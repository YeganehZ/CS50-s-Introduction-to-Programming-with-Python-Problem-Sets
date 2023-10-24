'''
Check out the link here for description:
https://cs50.harvard.edu/python/2022/psets/8/shirtificate/

'''

from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20) 

    def body(self):
        self.image("shirtificate.png", 5, 50, 200)
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        self.ln(60)
        self.cell(80)
        self.cell(30, 30, "Yeganeh Zamiri-Jafarian took CS50", align="C")



FPDF(orientation="P", unit="mm", format="A4")
pdf=PDF()
pdf.add_page()
pdf.body()
pdf.output("shirtificate.pdf")
