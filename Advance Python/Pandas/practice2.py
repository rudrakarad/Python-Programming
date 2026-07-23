import pandas as pd

data = {
    "Product" : ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Price" : [55000, 800, 2500, 12000, 9500],
    "Stock" : [15, 80, 45, 20, 10],
}

df = pd.DataFrame(data)

print(df)
print(df.Product)
print(df[["Product" , "Price"]])
print(df.head(3))
print(df.tail(2))
print(df.loc[3])
print(df.iloc[1])
print(df.loc[2, "Price"])
print(df.iloc[:4, 1:])
df.iloc[4,1] = 10000
print(df.sort_values(by="Price", ascending=True))
print(df.sort_values(by="Stock", ascending=False))
print(df[df["Price"] > 5000])
print(df[df["Stock"] < 20])
print(df[(df["Price"] > 5000) & (df["Stock"] > 10) ])