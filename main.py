from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

pdf.set_font(family="helvetica", size=16)
pdf.add_page()

# You can add text through cells
pdf.cell(w=0, h=12, txt="Hello world 1", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi there 2", align="L", ln=1, border=1)

pdf.output("output.pdf")
print("PDF successfully created")