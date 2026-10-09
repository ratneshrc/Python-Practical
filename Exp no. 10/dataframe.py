import pandas as pd

data = pd.read_csv("student.csv")

df = pd.DataFrame(data)

print("DataFrame:")
print(df)