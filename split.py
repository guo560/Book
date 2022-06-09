from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def pdf_split_2(pdf_input, fname, start, end):
    pdf = PdfFileReader(pdf_input)
    pdf_writer = PdfFileWriter()
    output_filename = r'\{}_{}-{}.pdf'.format(fname,start,end)
    # output_filename = os.path.join(path_output, '{}_{}-{}.pdf'.format(fname,start,end))  # 等价

    for page in range(start, end):
        pdf_writer.addPage(pdf.getPage(page))

    with open("F:\\Book"+"\\"+output_filename, 'wb') as out:
        pdf_writer.write(out)
        # print('生成文件:{}'.format(output_filename))


file_names = ["Primer C++(第5版)", "编译原理（第2版）", "计算机组成与设计：硬件软件接口"]
splits = [2, 6, 2]

for file_name, split in zip(file_names, splits):
    with open(file_name+".pdf", 'rb') as pdf:
        pdf_reader = PdfFileReader(pdf)
        pages = pdf_reader.numPages
        nums = pages // split
        for i in range(split):
            pdf_split_2(pdf, file_name, i*nums, min((i+1)*nums, pages))
