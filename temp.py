import pandas as pd

companies = pd.read_excel("data/processed/companies_clean.xlsx")

print("Total Companies:", len(companies))
print("\nLast 15 Companies:")
print(companies[["id", "company_name"]].tail(15))