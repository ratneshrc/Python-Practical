import numpy as np

data = np.array([
    ('A', 550),
    ('B', 270),
    ('C', 600)
], dtype=[('Label', 'U10'), ('Value', 'i4')])

print(data)
print("Labels:", data['Label'])
print("Values:", data['Value'])