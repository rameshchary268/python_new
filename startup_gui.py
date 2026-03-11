import tkinter as tk
from tkinter import messagebox

def greet():
    name = entry_name.get()
    if name:
        result_label.config(text=f"Hello, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter a name.")

def farewell():
    name = entry_name.get()
    if name:
        result_label.config(text=f"Goodbye, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter a name.")

def add_numbers():
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        result_label.config(text=f"Sum: {a + b}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def multiply_numbers():
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        result_label.config(text=f"Product: {a * b}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def clear_inputs():
    entry_name.delete(0, tk.END)
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="")

def about_app():
    messagebox.showinfo("About", "Startup GUI App\nCreated by Ramesh with Copilot.\nFeatures: Greeting, Farewell, Math operations.")

# GUI setup
root = tk.Tk()
root.title("Startup GUI App")

# Name input
tk.Label(root, text="Enter Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Number inputs
tk.Label(root, text="Enter Number 1:").grid(row=1, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Enter Number 2:").grid(row=2, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Greet", command=greet).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Farewell", command=farewell).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Add", command=add_numbers).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="Multiply", command=multiply_numbers).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Clear", command=clear_inputs).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="About", command=about_app).grid(row=5, column=1, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
