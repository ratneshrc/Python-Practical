import matplotlib.pyplot as plt


subjects = ['Maths', 'Science', 'English', 'Computer']
marks = [30, 25, 20, 25]


plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%',
    colors=['skyblue', 'lightgreen', 'orange', 'pink'],
    startangle=90
)


plt.title('Marks Distribution')


plt.show()