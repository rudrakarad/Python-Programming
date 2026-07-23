import pandas as pd

data = {
    "Name" : ["Rudra", "Manali", "Aryan", "Samyak"],
    "Age" : [18, 19, 18, 18],
    "Marks" : [92, 81, 76, 89],
}

df = pd.DataFrame(data)

print(df)
print(df.Name)
print(df[["Name", "Marks"]])
print(df.head(2))
print(df.tail(2))
print(df.loc[1])
print(df.iloc[2])
print(df.loc[2, "Marks"])
print(df.iloc[:3, :2])
df.iloc[3, 2] = 95
print(df)