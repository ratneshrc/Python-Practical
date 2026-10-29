import tkinter as tk

window = tk.Tk()
window.title("Subtraction")
window.geometry("400x300")

def subtract():
    a = int(e1.get())
    b = int(e2.get())
    label.config(text="Answer: " + str(a - b))

e1 = tk.Entry(window)
e1.pack(pady=10)

e2 = tk.Entry(window)
e2.pack(pady=10)

button = tk.Button(window, text="Subtract", command=subtract)
button.pack(pady=10)

label = tk.Label(window, text="")
label.pack()

window.mainloop()