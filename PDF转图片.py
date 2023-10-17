# PDF to Images
# pip install PyMuPDF
import fitz  # 导入PyMuPDF库
import os

# 将工作目录更改为包含PDF文件的目录
os.chdir("D:\QL\study")


def pdf_to_images(pdf_file):  # 处理PDF文件的路径
    # 新建文件夹
    folder_name = "PDF_images"
    os.mkdir(folder_name)
    # 打开文件
    doc = fitz.open(pdf_file)
    for p in doc:
        pix = p.get_pixmap()
        # 输出到指定文件夹（图片的输出路径，使用os.path.join拼接文件夹名称）
        output = os.path.join(folder_name, f"page{p.number+1}.png")
        pix.save(output)


pdf_to_images("Python编程：从入门到实践.pdf")
