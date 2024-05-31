import pandas as pd
import glob

filePaths = glob.glob("invoices/*.xlsx")

for filePath in filePaths:
    df = pd.read_excel(filePath, sheet_name="Sheet 1")
    print(df)