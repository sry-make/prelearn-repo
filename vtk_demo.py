import vtk

# 创建一个立方体
cube = vtk.vtkCubeSource()

# 创建一个映射器
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cube.GetOutputPort())

# 创建一个演员（actor）
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# 创建一个渲染器和一个渲染窗口
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

# 创建一个渲染窗口交互器
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# 添加演员到渲染器中
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)  # 设置背景颜色

# 开始渲染
renderWindow.Render()
renderWindowInteractor.Start()
