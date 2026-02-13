import pandas as pd
import numpy as np

#Readfile
df = pd.read_csv("sales.csv", sep="\t")
df.columns = df.iloc[0]
df = df[1:]
df.reset_index(drop=True, inplace=True)

#Convertcolumns
df["Quantity"] = df["Quantity"].astype(int)
df["Price"] = df["Price"].astype(int)

print("Corrected Data:\n")
print(df)

#Addtotalcolumn
df["Total"] = df["Quantity"] * df["Price"]

#NumPycalculations
daily_sales = df["Total"].values

print("\nTotal Sales:", np.sum(daily_sales))
print("Average Daily Sales:", np.mean(daily_sales))
print("Standard Deviation:", np.std(daily_sales))

# BSproduct
product_sales = df.groupby("Product")["Quantity"].sum()
best_product = product_sales.idxmax()

print("\nBest Selling Product:", best_product)
