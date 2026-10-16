
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]


plt.plot(x, y, marker='o', color='blue', label='My Data')


plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("My First Matplotlib Graph")


plt.legend()
plt.grid(True)


plt.show()
