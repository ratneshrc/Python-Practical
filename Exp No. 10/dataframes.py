import pandas as pd
from datetime import date


data = pd.read_csv("age.csv")


data["Birthdate"] = pd.to_datetime(data["Birthdate"])


today = date.today()

data["Age"] = data["Birthdate"].apply(
    lambda birthdate: today.year - birthdate.year -
    ((today.month, today.day) < (birthdate.month, birthdate.day))
)


print("Student Data:")
print(data)