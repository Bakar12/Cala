import tkinter as tk
import math
import re
import matplotlib.pyplot as plt
import numpy as np

def format_expression(expression):
    # Replace '^' with '**' for exponentiation
    expression = expression.replace('^', '**')

    # Format square root operations
    expression = re.sub(r'√\(?(\d+(\.\d+)?)\)?', r'math.sqrt(\1)', expression)

    # Format trigonometric functions
    for trig_func in ['sin', 'cos', 'tan']:
        expression = re.sub(rf'{trig_func}\((.*?)\)', rf'math.{trig_func}(math.radians(\1))', expression)

    return expression

def on_click(char):
    if char == '=':
        try:
            expression = display.get()
            formatted_expression = format_expression(expression)
            result = eval(formatted_expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, f"Error: {str(e)}")
    elif char == 'C':
        display.delete(0, tk.END)
    elif char == '←':
        if display.get().startswith("Error: "):
            display.delete(0, tk.END)
        else:
            display.delete(len(display.get())-1, tk.END)
    else:
        if display.get().startswith("Error: "):
            display.delete(0, tk.END)
        display.insert(tk.END, char)

def create_button(master, text, row, col, width=5, height=2, font=("Arial", 14), bg="#DDDDDD", fg="#000000"):
    """ Helper function to create a styled button """
    b = tk.Button(master, text=text, command=lambda char=text: on_click(char), width=width, height=height, font=font, bg=bg, fg=fg)
    b.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    return b

# Set up the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#333333")

# Set grid weight for better resizing
root.grid_columnconfigure(0, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Create the display
display = tk.Entry(root, width=21, font=("Arial", 24), bg="#EEEEEE", fg="#333333")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

# Create the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('←', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), (')', 4, 4),
    ('sin(', 5, 0), ('cos(', 5, 1), ('tan(', 5, 2), ('√', 5, 3), ('^', 5, 4),
    ('%', 6, 0)
]

for (text, row, col) in buttons:
    create_button(root, text, row, col)

# Run the application
root.mainloop()
