import sys
from openpyxl import load_workbook
from pathlib import Path

if len(sys.argv) < 3:
    print("Usage: python DDexcelwrite.py <email> <password>")
    sys.exit(1)

email = sys.argv[1]
password = sys.argv[2]

# Absolute path to Excel file (VERY IMPORTANT)
excel_path = Path(__file__).parent / "DDtestdataCS2.xlsx"

print(f"Writing to Excel file at: {excel_path}")

wb = load_workbook(excel_path)
ws = wb.active
ws.append([email, password])
wb.save(excel_path)

print("Data written successfully.")
