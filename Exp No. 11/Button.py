import tkinter as tk
from tkinter import messagebox

def show_message():
    name = entry.get()
    messagebox.showinfo("Message", "Welcome " + name)

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")

label = tk.Label(root, text="Enter Your Name:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_message)
button.pack(pady=10)

root.mainloop()