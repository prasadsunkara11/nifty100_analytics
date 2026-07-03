import pandas as pd
import os

folder = "data/processed"

for file in os.listdir(folder):

    if file.endswith(".xlsx"):

        print("=" * 60)
        print(file)

        df = pd.read_excel(
            os.path.join(folder, file)
        )

        print(df.columns.tolist())