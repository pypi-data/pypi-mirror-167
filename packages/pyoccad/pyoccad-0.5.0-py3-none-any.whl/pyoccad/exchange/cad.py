"""Interface module to export the geometric entities to external formats.
"""
import os
from typing import Union, Iterable

from OCC.Core.Geom import Geom_Geometry
from OCC.Core.IGESControl import IGESControl_Controller, IGESControl_Writer
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.TopoDS import TopoDS_Shape


def check_extension(filename: str, extension: str) -> str:
    """Checks that `filename` has required extension.
    If not, actual extension is replaced by the required one.

    Returns
    -------
    - filename [str]:
        Modified file name with required extension.
    """
    prefix, ext = os.path.splitext(filename)
    if ext != f".{extension}":
        filename = f"{prefix}.{extension}"
    return filename


def to_iges(
    shapes: Iterable[Union[Geom_Geometry, TopoDS_Shape]],
    filename: str,
    scale_factor: float = 1e3,
) -> bool:
    """Export shapes to IGES file.

    Parameters
    ----------
    - shapes, Iterable[Union[Geom_Geometry, TopoDS_Shape]]:
        The shapes to export
    - filename, str:
        File name (extension is automatically set to .igs)
    - scale_factor, float, optional:
        Scale factor, iges files are in millimetres (default: {1000})

    Returns
    -------
    - success, bool:
        `True` if written with success
    """
    from pyoccad.transform import Scale

    IGESControl_Controller().Init()
    writer = IGESControl_Writer('MM', 0)

    for shape in shapes:
        if isinstance(shape, Geom_Geometry):
            writer.AddGeom(Scale.from_factor(shape, scale_factor, False))
        elif isinstance(shape, TopoDS_Shape):
            writer.AddShape(Scale.from_factor(shape, scale_factor, False))
        else:
            raise TypeError(f"Unsupported type {type(shape).__name__!r}")

    writer.ComputeModel()
    filename = check_extension(filename, "igs")

    return writer.Write(filename)


# TODO: add mode enum visible/wrapped from occt
def to_step(
    shapes: Iterable[TopoDS_Shape],
    filename: str,
    mode = STEPControl_AsIs,
    scale_factor: float = 1e3
) -> bool:
    """Export shapes to STEP file.

    Parameters
    ----------
    - shapes, Iterable[TopoDS_Shape]:
        The shapes to save
    - filename, str:
        File name (extension is automatically set to .stp)
    - mode:
    - scale_factor, float, optional:
        Scale factor, step files are in millimetres (default: {1000})

    Returns
    -------
    flag : bool
        `True` if written with success
    """
    from pyoccad.transform import Scale

    writer = STEPControl_Writer()

    for shape in shapes:
        if isinstance(shape, TopoDS_Shape):
            writer.Transfer(Scale.from_factor(shape, scale_factor, False), mode)
        else:
            raise TypeError(f"Unsupported type {type(shape).__name__!r}")

    filename = check_extension(filename, "stp")

    return writer.Write(filename)
