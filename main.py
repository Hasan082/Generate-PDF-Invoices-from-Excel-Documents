import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filePaths = glob.glob("invoices/*.xlsx")

for filePath in filePaths:
    df = pd.read_excel(filePath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    fileName = Path(filePath).stem
    invoiceNo = fileName.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoices No:- {invoiceNo}", ln=1)
    pdf.output(f"pdfs/{fileName}.pdf")
