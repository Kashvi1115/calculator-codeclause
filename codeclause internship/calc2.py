import tkinter as tk

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, round(result, 3))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=20, font=('Arial', 14), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val, padx=3, pady=3)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(window, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val, padx=3, pady=3)

tk.Button(window, text="=", width=5, height=2, command=calculate).grid(row=row_val, column=col_val + 1, columnspan=2, padx=3, pady=3)

window.mainloop()
