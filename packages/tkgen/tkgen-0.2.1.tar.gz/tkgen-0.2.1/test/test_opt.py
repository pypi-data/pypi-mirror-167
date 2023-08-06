from pyskema import Node, AtomType
from tkgen import make_form

schema = Node.of_record(
    {
        "a": Node.of_record(
            {
                "b": Node.of_atom(AtomType.INT),
                "c": Node.of_atom(AtomType.INT),
            },
            optional=True,
            default={"b": 4, "c": 5},
        ),
        "d": Node.of_atom(AtomType.INT, optional=True, default=42),
    }
)

win = make_form(schema, print)
win.mainloop()
