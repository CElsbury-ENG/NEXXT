import pandas as pd

# Ensure the data folder exists
import os
os.makedirs('data', exist_ok=True)

# Create an empty DataFrame and write to a valid .xlsx file
df = pd.DataFrame()
df.to_excel('data/responses.xlsx', index=False, engine='openpyxl')
print("Created data/responses.xlsx successfully.")