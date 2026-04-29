import tkinter as tk
from tkinter import messagebox

# ---- Logic Functions ----
def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def subtract_numbers(a, b):
    return a - b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# ---- GUI Action Functions ----
def handle_greet():
    name = name_entry.get().strip()
    if name:
        result_label.config(text=greet(name))
    else:
        messagebox.showwarning("Input Error", "Please enter a name")

def handle_farewell():
    name = name_entry.get().strip()
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

def handle_subtract():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        result_label.config(text=f"Difference: {subtract_numbers(a, b)}")
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers")

def handle_divide():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        result_label.config(text=f"Quotient: {divide_numbers(a, b)}")
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers")

def clear_result():
    result_label.config(text="")


# ---- GUI Setup ----
root = tk.Tk()
root.title("Startup GUI App")
root.geometry("400x400")

# ---- Name Section ----
name_frame = tk.LabelFrame(root, text="Name Section", padx=10, pady=10)
name_frame.pack(pady=10, fill="x")

tk.Label(name_frame, text="Enter Name:").pack(pady=5)
name_entry = tk.Entry(name_frame)
name_entry.pack()

tk.Button(name_frame, text="Greet", command=handle_greet).pack(pady=2)
tk.Button(name_frame, text="Farewell", command=handle_farewell).pack(pady=2)

# ---- Numbers Section ----
num_frame = tk.LabelFrame(root, text="Numbers Section", padx=10, pady=10)
num_frame.pack(pady=10, fill="x")

tk.Label(num_frame, text="Number 1:").pack(pady=5)
num1_entry = tk.Entry(num_frame)
num1_entry.pack()

tk.Label(num_frame, text="Number 2:").pack(pady=5)
num2_entry = tk.Entry(num_frame)
num2_entry.pack()

tk.Button(num_frame, text="Add", command=handle_add).pack(pady=2)
tk.Button(num_frame, text="Subtract", command=handle_subtract).pack(pady=2)
tk.Button(num_frame, text="Multiply", command=handle_multiply).pack(pady=2)
tk.Button(num_frame, text="Divide", command=handle_divide).pack(pady=2)

# ---- Result ----
result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
result_label.pack(pady=15)

# ---- Utility Buttons ----
tk.Button(root, text="Clear Result", command=clear_result).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

# ---- Run App ----
root.mainloop()
