import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filePaths = glob.glob("invoices/*.xlsx")

for filePath in filePaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Extract file path
    fileName = Path(filePath).stem

    # Extract invoice number and date
    invoiceNo, invoiceDate = fileName.split("-")

    # Add Invoice Number to pdf
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoices No:- {invoiceNo}", ln=1)
    # Add Invoice Date to pdf
    pdf.set_font(family="Times", size=12)
    pdf.cell(w=50, h=8, txt=f"Date:- {invoiceDate}", ln=1)

    # Extract data from excel
    df = pd.read_excel(filePath, sheet_name="Sheet 1", engine="openpyxl")

    # Add header to the pdf
    pdf.ln(6)
    columns = list(df.columns)
    columns = [column.replace("_", " ").title() for column in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=35, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=33, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10, style="B")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=35, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=33, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1)
        pdf.ln(8)

    # Output pdf
    pdf.output(f"pdfs/{fileName}.pdf")
