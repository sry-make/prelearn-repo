# main.py
from src.step_converter import convert_step_to_stl
from src.vtk_renderer import render_stl


def main():
    step_file = 'data/input/xjtu_full.STEP'
    stl_file1 = 'data/output/output_model.stl'
    stl_file2 = 'data/output/soft_generate'
    # 将STEP文件转换为STL文件
    convert_step_to_stl(step_file, stl_file1)

    # 渲染STL文件
    render_stl(stl_file2)


if __name__ == "__main__":
    main()
