import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 15, 12, 20, 18, 25, 22, 30]


plt.scatter(
    x, y,
    color='blue',
    marker='o',
    s=100,
    label='Data Points'
)

plt.title('Simple Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')


plt.grid(True)
plt.legend()


plt.show()