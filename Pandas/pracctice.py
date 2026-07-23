import pandas as pd

a = {
    "name" : ["Rudra", "Manali", "Aryan", "Samyak"],
    "age" : [18, 19, 18, 18],
    "marks" : [92, 81, 76, 89],
}

df = pd.DataFrame(a)
print(df)
print(df.name)
print(df.age, df.marks)
print(df.name[:3])
print(df.name[2:])
print(df.shape)