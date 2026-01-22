import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


csv_path = Path('housing.csv')
if not csv_path.exists():
    raise FileNotFoundError("No se encontró 'housing.csv' en el directorio actual")
df = pd.read_csv(csv_path)
# print(df.head())
# print(df.info())
# print(df["ocean_proximity"].value_counts())

df.hist(bins=50, figsize=(20,15))
plt.show()