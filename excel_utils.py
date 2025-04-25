import pandas as pd
import os

EXCEL_PATH = 'data/responses.xlsx'
SHEET = 'Sheet1'
ENGINE = 'openpyxl'

def load_data():
    try:
        return pd.read_excel(EXCEL_PATH, sheet_name=SHEET, engine=ENGINE)
    except (FileNotFoundError, ValueError):
        # If file missing or sheet missing, return empty DataFrame
        return pd.DataFrame()

def append_response(resp: dict):
    # Ensure data folder exists
    os.makedirs(os.path.dirname(EXCEL_PATH), exist_ok=True)

    # Load existing data
    df = load_data()

    # Create a DataFrame from the single response
    new_row = pd.DataFrame([resp])

    # Concatenate onto existing
    df = pd.concat([df, new_row], ignore_index=True)

    # Write back to Excel
    df.to_excel(EXCEL_PATH, sheet_name=SHEET, index=False, engine=ENGINE)