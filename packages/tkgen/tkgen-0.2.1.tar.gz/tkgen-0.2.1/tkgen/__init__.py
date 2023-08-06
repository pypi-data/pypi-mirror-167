from itertools import count

__version__ = "0.2.1"

from tkinter import (
    Tk,
    Toplevel,
    LEFT,
    RIGHT,
    W,
    E,
    TOP,
    X,
    Y,
    SOLID,
    NSEW,
    StringVar,
    IntVar,
    DoubleVar,
    BooleanVar,
    Listbox,
)
import tkinter.ttk as tk
from tkinter.messagebox import askokcancel

from pyskema.schema import Atom, AtomType, Node
from pyskema.validate import validate
from pyskema.visitor import Visitor

from .tooltip import Tooltip


def make_form(schema, callback, *, Window=Tk, title=None, init_data=None):
    return FormFactory.make_toplevel(schema, callback, Window=Window, title=title, init_data=init_data)


class FormFactory(Visitor):
    @classmethod
    def make_toplevel(cls, schema, callback, *, Window=Tk, title=None, init_data=None):
        pipe = Pipe()

        def cancel():
            callback(None)
            master.destroy()

        def extract():
            callback(pipe.pull())
            master.destroy()

        master = Window()
        if title:
            master.title(title)

        main_frame = tk.Frame(master)
        main_frame.pack(side=TOP)

        form_frame = tk.Frame(main_frame)
        form_frame.pack(side=LEFT)

        scroll = tk.Scrollbar(main_frame)
        scroll.pack(side=LEFT, fill=Y)

        button_frame = tk.Frame(master)
        button_frame.pack(side=TOP, fill=X)

        b_cancel = tk.Button(button_frame, text="Cancel", command=cancel)
        b_ok = tk.Button(button_frame, text="Validate", command=extract)

        b_cancel.pack(side=LEFT)
        b_ok.pack(side=LEFT)

        res = cls().visit(schema, form_frame, pipe)

        if isinstance(schema.structure, Atom):
            Tooltip(res, text=schema.description)

        if init_data is not None:
            pipe.push(init_data)

        return master

    def visit_atom(self, atom, parent, pipe, *args):
        if atom.type_ == AtomType.STR:
            v = StringVar()
            w = tk.Entry(parent, textvariable=v)

        elif atom.type_ == AtomType.BOOL:
            v = BooleanVar()
            w = tk.Checkbutton(parent, text="", variable=v)

        elif atom.type_ == AtomType.FLOAT:
            v = DoubleVar()
            w = tk.Spinbox(parent, textvariable=v, incr=0.1)

        elif atom.type_ == AtomType.INT:
            v = IntVar()
            w = tk.Spinbox(parent, textvariable=v)

        elif atom.type_ == AtomType.OPTION:
            if len(atom.options) == 1:
                w = tk.Label(parent, text=atom.options[0])
                v = StringVar()
                v.set(atom.options[0])
            else:
                v = StringVar()
                v.set(atom.options[0])
                w = tk.OptionMenu(parent, v, *atom.options)

        else:
            raise NotImplementedError(f"{atom.type_} is not supported yet.")

        @pipe.puller
        def pull():
            return v.get()

        @pipe.pusher
        def push(data):
            return v.set(data)

        w.pack(anchor=W, side=TOP)
        return w

    def visit_union(self, union, parent, pipe, *args):
        frame = tk.Frame(parent)
        select_var = IntVar()
        options = []
        pipes = [Pipe() for _ in union.options]

        for i, node in enumerate(union.options):
            if isinstance(node.structure, Atom):
                sub_frame = tk.Frame(frame)
                radio = tk.Radiobutton(sub_frame, variable=select_var, value=i)
                radio.pack(anchor=W, side=LEFT)
                field = self.visit(node, sub_frame, pipes[i])
                field.pack(anchor=E, side=RIGHT)
                sub_frame.pack(anchor=W, side=TOP, fill=X)
                options.append(sub_frame)
                if node.description:
                    Tooltip(radio, text=node.description)
            else:
                radio = tk.Radiobutton(frame, variable=select_var, value=i)
                sub_frame = LabelWidgetFrame(frame, radio)
                sub_frame.pack(anchor=W, side=TOP, fill=X)
                options.append(self.visit(node, sub_frame, pipes[i]))
                if node.description:
                    Tooltip(sub_frame.label_widget, text=node.description)

        @pipe.puller
        def pull():
            sel = select_var.get()
            return pipes[sel].pull()

        @pipe.pusher
        def push(data):
            op, _ = validate(data, Node(union))

            i = union.options.index(op)

            pipes[i].push(data)

            select_var.set(i)

        frame.pack(anchor=W, side=TOP, fill=X)
        return frame

    def visit_record(self, rec, parent, pipe, *args):
        frame = tk.Frame(parent)
        pipes = {key: Pipe() for key in rec.fields}

        for key, node in rec.fields.items():
            if isinstance(node.structure, Atom):
                field_frame = tk.Frame(frame)
                label = tk.Label(field_frame, text=key)
                label.pack(anchor=W, side=LEFT)
                field = self.visit(node, field_frame, pipes[key])
                field.pack(anchor=E)
                if node.description:
                    Tooltip(field_frame, text=node.description)
            elif node.optional:
                field_frame = FoldableLabelFrame(frame, text=key)
                if node.description:
                    Tooltip(field_frame.label_widget, text=node.description)
                self.visit(node, field_frame.content, pipes[key])
            else:
                label = tk.Label(frame, text=key)
                field_frame = LabelWidgetFrame(frame, label)
                if node.description:
                    Tooltip(label, text=node.description)
                self.visit(node, field_frame, pipes[key])

            if node.optional:
                pipes[key].push(node.default)

            field_frame.pack(anchor=W, side=TOP, fill=X)

        @pipe.puller
        def pull():
            return {key: p.pull() for key, p in pipes.items()}

        @pipe.pusher
        def push(data):
            for key, d in data.items():
                pipes[key].push(d)

        frame.pack(anchor=W, side=TOP, fill=X)
        return frame

    def visit_collection(self, collection, parent, pipe, *args):
        frame = tk.Frame(parent)
        frame.pack(anchor=W, side=TOP, fill=X)
        data_storage = {}

        lock = Flag(False)

        def add_item(data):
            name = get_name(data)
            listbox.insert(len(data_storage), name)
            data_storage[name] = data

        def delete_item(i):
            name = listbox.get(i)
            listbox.delete(i)
            del data_storage[name]

        def new():
            if lock:
                return

            def cb(data):
                if data is not None:
                    add_item(data)
                lock.off()
                form.destroy()

            lock.on()
            form = FormFactory.make_toplevel(collection.element, cb, title="New element...", Window=Toplevel)

        def edit():
            if lock:
                return

            name = listbox.get(listbox.curselection())

            def cb(data):
                if data is not None:
                    data_storage[name] = data
                lock.off()
                form.destroy()

            init_data = data_storage[name]
            lock.on()
            form = FormFactory.make_toplevel(
                collection.element, cb, title="Edit element...", Window=Toplevel, init_data=init_data
            )

        def remove():
            if lock:
                return

            delete_item(listbox.curselection())

        button_frame = tk.Frame(frame)
        button_frame.pack(side=LEFT)

        buttons = [
            tk.Button(button_frame, text="+", command=new),
            tk.Button(button_frame, text="E", command=edit),
            tk.Button(button_frame, text="-", command=remove),
        ]

        for b in buttons:
            b.pack(side=TOP, fill=X)

        listbox = Listbox(frame, height=7, selectmode="browse")
        listbox.pack(side=LEFT)

        @pipe.puller
        def pull():
            n = len(data_storage)
            return [data_storage[name] for name in listbox.get(0, n)]

        @pipe.pusher
        def push(data):
            while data_storage:
                delete_item(0)

            for d in data:
                add_item(d)

        return frame

    def visit_map(self, map_, parent, pipe, *args):
        frame = tk.Frame(parent)
        frame.pack(anchor=W, side=TOP, fill=X)

        data_storage = {}

        lock = Flag(False)

        def add_item(key, data):
            listbox.insert(len(data_storage), key)
            data_storage[key] = data

        def delete_item(i):
            name = listbox.get(i)
            listbox.delete(i)
            del data_storage[name]

        subform_sch = Node.of_record(
            {
                "name": Node.of_atom(AtomType.STR),
                "value": map_.element,
            }
        )

        def new():
            if lock:
                return

            def cb(data):
                if data is not None:
                    key = data["key"]
                    elem = data["element"]
                    add_item(key, elem)
                lock.off()
                form.destroy()

            lock.on()

            form = FormFactory.make_toplevel(subform_sch, cb, Window=Toplevel)

        def edit():
            if lock:
                return

            name = listbox.get(listbox.curselection())

            def cb(data):
                if data is not None:
                    data_storage[name] = data
                lock.off()
                form.destroy()

            init_data = data_storage[name]
            lock.on()
            form = FormFactory.make_toplevel(
                subform_sch,
                cb,
                Window=Toplevel,
                init_data={"element": init_data, "key": name},
            )

        def remove():
            if lock:
                return

            delete_item(listbox.curselection())

        button_frame = tk.Frame(frame)
        button_frame.pack(side=LEFT)

        buttons = [
            tk.Button(button_frame, text="+", command=new),
            tk.Button(button_frame, text="E", command=edit),
            tk.Button(button_frame, text="-", command=remove),
        ]

        for b in buttons:
            b.pack(side=TOP, fill=X)

        listbox = Listbox(frame, height=7, selectmode="browse")
        listbox.pack(side=LEFT)

        @pipe.puller
        def pull():
            n = len(data_storage)
            return [data_storage[name] for name in listbox.get(0, n)]

        @pipe.pusher
        def push(data):
            while data_storage:
                delete_item(0)

            for k, d in data.items():
                add_item(k, d)
        return frame

    def visit_tuple(self, tup, parent, pipe, *args):
        frame = tk.Frame(parent)
        pipes = tuple(Pipe() for _ in tup.fields)

        for i, node in enumerate(tup.fields):
            sub = tk.Frame(frame)
            self.visit(node, sub, node.description, pipes[i])
            sub.pack(anchor=W, side=TOP, fill=X)
            if node.description:
                Tooltip(sub, text=node.description)


        frame.pack(anchor=W, side=TOP, fill=X)

        @pipe.puller
        def pull():
            return tuple(p.pull() for p in pipes)

        @pipe.pusher
        def push(data):
            assert len(data) == len(pipes)

            for e, p in zip(data, pipes):
                p.push(e)
        return frame


class LabelWidgetFrame(tk.LabelFrame):
    """Create a frame with a widget label in the parent."""

    def __init__(self, parent, label_widget):
        super().__init__(parent)
        self.label_widget = label_widget
        self.configure(labelwidget=label_widget)


class FoldableLabelFrame(LabelWidgetFrame):
    def __init__(self, parent, text):
        label_widget = tk.Frame(parent)
        self.v = BooleanVar()
        ck = tk.Checkbutton(label_widget, variable=self.v, command=self.change)
        ck.pack(side=LEFT)
        label = tk.Label(label_widget, text=text)
        label.pack(side=LEFT)
        super().__init__(parent, label_widget)

        self.toggle = ck
        self.content = tk.Frame(self)
        self.alt_cont = tk.Label(self, text="default")
        self.alt_cont.pack()

    def change(self):
        if self.v.get():
            self.alt_cont.forget()
            self.content.pack()
        else:
            self.content.forget()
            self.alt_cont.pack()


class Pipe:
    def __init__(self):
        self._puller = None
        self._pusher = None

    def puller(self, fn):
        self._puller = fn

    def pusher(self, fn):
        self._pusher = fn

    def pull(self):
        return self._puller()

    def push(self, data):
        self._pusher(data)


class Flag:
    def __init__(self, initial=False):
        self._on = initial

    def on(self):
        self._on = True

    def off(self):
        self._on = False

    def __bool__(self):
        return self._on


def get_name(data):
    return str(data)
