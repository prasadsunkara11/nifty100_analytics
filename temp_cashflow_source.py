import pandas as pd

df = pd.read_excel("data/processed/cashflow_clean.xlsx")

abb = df[df["company_id"] == "ABB"]

print(abb)
print("\nRows:", len(abb))