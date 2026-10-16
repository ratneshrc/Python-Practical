import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5]
temperature = [25, 28, 26, 30, 32]


plt.plot(
    days,
    temperature,
    color='blue',
    marker='o',
    linestyle='-',
    linewidth=2,
    label='Temperature'
)


plt.title('Temperature Over 5 Days')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')


plt.grid(True)
plt.legend()


plt.show()