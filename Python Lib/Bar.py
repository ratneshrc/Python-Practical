import matplotlib.pyplot as plt


students = ['A', 'B', 'C', 'D', 'E']
marks = [85, 70, 90, 65, 80]


plt.bar(students, marks, color='skyblue', edgecolor='black')


plt.title('Students Marks')
plt.xlabel('Students')
plt.ylabel('Marks')


plt.grid(axis='y', linestyle='--', alpha=0.5)


plt.show()