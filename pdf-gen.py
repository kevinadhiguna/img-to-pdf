import glob
from fpdf import FPDF

imagelist = glob.glob('images/*.jpg')

pdf = FPDF()

for image in imagelist:
    pdf.add_page()
    pdf.image(image, 10,210,297)
pdf.output("yourfile.pdf", "F")
