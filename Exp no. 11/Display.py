import tkinter as tk

window = tk.Tk()
window.title("Message")
window.geometry("400x300")

label = tk.Label(window, text="Welcome to Python GUI")
label.pack(pady=30)

button = tk.Button(window, text="Exit", command=window.destroy)
button.pack()

window.mainloop()