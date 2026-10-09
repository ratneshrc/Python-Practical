import pandas as pd

data = pd.read_csv("students.csv")

series = data["Name"]

print("Series")
print(series)