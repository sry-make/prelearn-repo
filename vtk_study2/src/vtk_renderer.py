# src/vtk_renderer.py
import vtk

def render_stl(stl_filename):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(stl_filename)
    reader.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)

    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(render_window)

    renderer.AddActor(actor)
    renderer.SetBackground(0.1, 0.2, 0.3)

    render_window.Render()
    render_window_interactor.Start()
