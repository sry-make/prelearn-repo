# src/step_converter.py
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Core.StlAPI import StlAPI_Writer


def convert_step_to_stl(step_filename, stl_filename):
    step_reader = STEPControl_Reader()
    step_reader.ReadFile(step_filename)
    step_reader.TransferRoots()
    shape = step_reader.Shape()

    BRepMesh_IncrementalMesh(shape, 0.1)

    stl_writer = StlAPI_Writer()
    stl_writer.Write(shape, stl_filename)
    print(f"Converted {step_filename} to {stl_filename}")
