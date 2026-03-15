
import pandas as pd
data = {
    "Name": ["Ali", "Amina", "Hassan"],
    "Age": [25, 22, 24],
    "Score": [80, 90, 85]
}

df = pd.DataFrame(data)
print(df)

print(df.head())     
print(df.tail())     
print(df.shape)     
print(df.columns)  
df = pd.read_csv("students.csv")
print(df.head())



