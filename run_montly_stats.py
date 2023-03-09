import pandas as pd
import pypistats
from tqdm import tqdm
import xlsxwriter


packages = ["oracle-ads", "ocifs"]

spreadsheet = "monthly_package_downloads.xlsx"

with pd.ExcelWriter(spreadsheet, datetime_format="YYYY-MM", engine='xlsxwriter') as writer:
    for package in tqdm(packages):
        df = pypistats.overall(package, total=True, format="pandas")
        df.set_index(pd.to_datetime(df.date)).groupby(pd.Grouper(freq="M")).sum(
            numeric_only=True
        ).to_excel(writer, sheet_name=package)
        
print(f"results written to: {spreadsheet}")