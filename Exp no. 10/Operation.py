import numpy as np
import pandas as pd
A = np.array([
    [10, 20],
    [30, 40]
])

B = np.array([
    [2, 4],
    [5, 8]
])

print("\n2D ARRAY A")
print(A)

print("\n 2D ARRAY B ")
print(B)


# Addition
print("\nAddition:")
print(A + B)


# Subtraction
print("\nSubtraction:")
print(A - B)


# Multiplication
print("\nMultiplication:")
print(A * B)


# Division
print("\nDivision:")
print(A / B)


# Transpose
print("\nTranspose of A:")
print(A.T)


# Exponential
print("\nExponential of A:")
print(np.exp(A))
