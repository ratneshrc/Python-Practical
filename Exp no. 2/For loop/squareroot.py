import math

n = int(input("Enter number: "))

root = int(math.sqrt(n))

count = 0

for i in range(2, root):
    if root % i == 0:
        count += 1

print("Square Root =", root)

if root > 1 and count == 0:
    print("Prime")
else:
    print("Not Prime")