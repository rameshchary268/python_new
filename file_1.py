import tkinter as tk
from tkinter import messagebox

# ---- Existing Logic Functions ----
def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b


# ---- GUI Action Functions ----
def handle_greet():
    name = name_entry.get()
    if name:
        result_label.config(text=greet(name))
    else:
        messagebox.showwarning("Input Error", "Please enter a name")

def handle_farewell():
    name = name_entry.get()
    if name:
        result_label.config(text=farewell(name))
    else:
        messagebox.showwarning("Input Error", "Please enter a name")

def handle_add():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        result_label.config(text=f"Sum: {add_numbers(a, b)}")
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers")

def handle_multiply():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        result_label.config(text=f"Product: {multiply_numbers(a, b)}")
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers")


# ---- GUI Setup ----
root = tk.Tk()
root.title("Startup GUI App")
root.geometry("350x350")

# ---- Name Section ----
tk.Label(root, text="Enter Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Button(root, text="Greet", command=handle_greet).pack(pady=2)
tk.Button(root, text="Farewell", command=handle_farewell).pack(pady=2)

# ---- Numbers Section ----
tk.Label(root, text="Number 1:").pack(pady=5)
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root, text="Number 2:").pack(pady=5)
num2_entry = tk.Entry(root)
num2_entry.pack()

tk.Button(root, text="Add", command=handle_add).pack(pady=2)
tk.Button(root, text="Multiply", command=handle_multiply).pack(pady=2)

# ---- Result ----
result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=15)

# ---- Run App ----
root.mainloop()
