import yaml

from tkgen import make_form

from pyskema import Node, AtomType

schema = Node.of_record(
    {
        "name": Node.of_atom(AtomType.STR, description="Prefix of the output name."),
        "store_cells": Node.of_atom(
            AtomType.BOOL,
            description="Store data in pickle's object.",
            optional=True,
            default=False,
        ),
        "main_dir": Node.of_atom(
            AtomType.STR,
            description="Path to the main directory, default directory is the current directory.",
            optional=True,
            default=".",
        ),
        "host_dir": Node.of_atom(
            AtomType.STR,
            description="Directory of the synthesized compound from the current path HOST.",
            optional=True,
            default="host",
        ),
        "compet_dir": Node.of_atom(
            AtomType.STR,
            description="Subdirectory of [main_dir] where competiting compound results are stored.",
            optional=True,
            default="compet",
        ),
        "phases": Node.of_collection(
            Node.of_atom(AtomType.STR, description="Name of the competiting compound directory under [main_dir]/."),
            description="List of competiting compound directories.",
        ),
        "phase_subdir": Node.of_atom(
            AtomType.STR,
            description="A relative path to the OUTCAR of the compound in [main_dir]/[compet_dir]/[phase_dir].",
            optional=True,
            default=".",
        ),
        "display_name": Node.of_map(
            Node.of_atom(AtomType.STR, description="Name to a LaTeX style name for the legend."),
            description=("Map folder names to legend names."),
            optional=True,
            default={},
        ),
        "mu_i": Node.of_map(
            Node.of_record(
                {
                    "dir": Node.of_atom(
                        AtomType.STR,
                        description="name of the corresponding phase directory.",
                    ),
                    "mui": Node.of_union(
                        [
                            Node.of_atom(
                                AtomType.OPTION,
                                options=["x", "y", "c"],
                                description=(
                                    "Specify how to vary the chemical potential in the diagram."
                                    "\n> 'x': varies mu_i along the x-axis"
                                    "\n> 'y': varies mu_i along the y-axis"
                                    "\n> 'c': constrain mu_i so that every (x, y) point respect the host."
                                    "\nNB1: for 2 species, define 'y' and 'c'"
                                    "\nNB2: for 3 species, define 'x', 'y' and 'c'"
                                    "\nNB3: for >3 species, define 'x', 'y' and 'c' for 3 species, set"
                                    "\nthe others to a given value."
                                ),
                            ),
                            Node.of_atom(
                                AtomType.FLOAT,
                                description="Set an arbitrary potential (eV).",
                            ),
                        ],
                        description=(
                            "Specify how this species must be used in the diagram."
                        ),
                    ),
                }
            ),
            description="Specify reference potentials.",
        ),
        "Dmu_plot": Node.of_atom(
            AtomType.BOOL,
            description="Use relative chemical potentials in the plot instead of absolute values.",
            optional=True,
            default=True,
        ),
        "plot": Node.of_record(
            {
                "limits": Node.of_union(
                    [
                        Node.of_atom(AtomType.OPTION, options=["auto"]),
                        Node.of_record(
                            {
                                "xmin": Node.of_atom(AtomType.FLOAT),
                                "xmax": Node.of_atom(AtomType.FLOAT),
                                "ymin": Node.of_atom(AtomType.FLOAT),
                                "ymax": Node.of_atom(AtomType.FLOAT),
                            }
                        ),
                    ],
                    description="Plot limits parameters.",
                    optional=True,
                    default="auto",
                ),
                "xstep": Node.of_atom(AtomType.FLOAT, optional=True, default=1.0),
                "ystep": Node.of_atom(AtomType.FLOAT, optional=True, default=2.0),
                "fontsize": Node.of_atom(AtomType.INT, optional=True, default=16),
                "title_fontsize": Node.of_atom(AtomType.INT, optional=True, default=18),
                "legend_fontsize": Node.of_atom(
                    AtomType.INT, optional=True, default=12
                ),
                "margins": Node.of_record(
                    {
                        "left": Node.of_atom(
                            AtomType.FLOAT, optional=True, default=0.05
                        ),
                        "right": Node.of_atom(
                            AtomType.FLOAT, optional=True, default=0.95
                        ),
                        "bottom": Node.of_atom(
                            AtomType.FLOAT, optional=True, default=0.2
                        ),
                        "top": Node.of_atom(AtomType.FLOAT, optional=True, default=0.8),
                        "wspace": Node.of_atom(
                            AtomType.FLOAT, optional=True, default=0.2
                        ),
                        "hspace": Node.of_atom(
                            AtomType.FLOAT, optional=True, default=0.2
                        ),
                    },
                    optional=True,
                    default={},
                ),
                "remove_title": Node.of_atom(
                    AtomType.BOOL, optional=True, default=False
                ),
                "save_figure_fmt": Node.of_atom(
                    AtomType.STR, optional=True, default="png"
                ),
                "show": Node.of_atom(AtomType.BOOL, optional=True, default=False),
            }
        ),
    }
)


def cb(data):
    if data is None:
        print("Abort.")
    else:
        print(yaml.dump(data))


app = make_form(schema, cb)

app.mainloop()
