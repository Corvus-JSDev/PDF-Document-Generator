from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

"""
pdf.set_font(family="helvetica", size=16)
pdf.add_page()

# You can add text through cells
pdf.cell(w=0, h=16, txt="Hello world 1", align="L", ln=1, border=1)
pdf.cell(w=0, h=16, txt="Hi there 2", align="C", ln=1, border=1)

pdf.set_font(family="times", size=16)
pdf.cell(w=60, h=16, txt="width=60 w/ center txt", align="C", ln=1, border=1)
pdf.cell(w=100, h=16, txt="width=100 w/ right txt", align="R", ln=1, border=1)
pdf.cell(w=80, h=16, txt="This has no break line (ln=0)", align="L", ln=0, border=1)
pdf.cell(w=0, h=25, txt="Height = 25", align="L", ln=1, border=1)


pdf.add_page()
pdf.cell(w=0, h=16, txt="This is a new page", align="L", ln=1, border=1)
pdf.cell(w=0, h=16, txt="Hi there", align="C", ln=1, border=1)
"""



pdf.output("output.pdf")
print("PDF successfully created")