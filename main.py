from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

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

data = pd.read_csv("topics.csv")


def add_footer(ln, title):
	pdf.ln(ln)
	pdf.set_font(family="Times", size=12, style="I")
	pdf.cell(txt=f"{title} | Page {page_number}", w=0, h=12, align="R", ln=1)


page_number = 1
for index, row in data.iterrows():
	# Generate the first page and its title
	pdf.set_font(family="Times", size=24, style="B")
	pdf.add_page()
	pdf.cell(txt=f"{index+1}. {row['Topic']}", w=0, h=24, align="L", ln=1)
	pdf.line(10, 28, 200, 28)

	# Add some basic text
	pdf.set_font(family="helvetica", size=16)
	pdf.cell(txt=f"This is page: 1 for {row['Topic']}", w=0, h=16, align="L", ln=1)

	# Add footer
	add_footer(230, row['Topic'])
	page_number += 1

	# Add additional pages if needed
	for x in range(1, row["Pages"]):
		pdf.set_font(family="helvetica", size=16)
		pdf.add_page()
		pdf.cell(txt=f"This is page: {x+1} for {row['Topic']}", w=0, h=16, align="L", ln=1)

		# Add footer
		add_footer(255, row['Topic'])
		page_number += 1


pdf.output("output.pdf")
print("PDF successfully created")