# Create Invoice PDFs from Excel by Python

This project contains a script to generate PDF invoices from Excel files. The script reads Excel files from a specified directory, extracts invoice details, and generates corresponding PDF files with the extracted data.

## Prerequisites

Ensure you have the following Python packages installed:

- `pandas`
- `fpdf`
- `openpyxl`
- `glob`
- `pathlib`

You can install the required packages using the following commands:

```bash
pip install pandas fpdf openpyxl
```

## Directory Structure

The project directory should have the following structure:

```
project_directory/
│
├── invoices/
│   ├── 10001-2023.01.18.xlsx
│   ├── 10002-2023.02.18.xlsx
│   └── 10003-2023.02.18.xlsx
│
├── pdfs/  (This directory will be created if it does not exist)
│
├── main.py
├── README.md
```

## How to Use

1. **Place your Excel files**: Ensure that your Excel files are placed in the `invoices` directory. The filenames should follow the format `invoiceNo-invoiceDate.xlsx` (e.g., `1234-20230101.xlsx`).

2. **Run the script**: Execute the `main.py` script to generate the PDF invoices. The PDFs will be saved in the `pdfs` directory.

```bash
python main.py
```

3. **Check the output**: The generated PDF files will be saved in the `pdfs` directory with the same names as the corresponding Excel files.

## Example

If you have an Excel file named `1234-2023.01.01.xlsx` in the `invoices` directory with the following content:

| Product Id | Product Name   | Amount Purchased | Price Per Unit | Total Price |
|------------|----------------|------------------|----------------|-------------|
| 101        | Product A      | 5                | 10             | 50          |
| 102        | Product B      | 2                | 20             | 40          |

The script will generate a PDF named `1234-20230101.pdf` in the `pdfs` directory with the same content formatted as a table.