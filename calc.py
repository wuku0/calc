import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=25)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0),
    ('8', 1, 1),
    ('9', 1, 2),
    ('+', 1, 3),
    ('4', 2, 0),
    ('5', 2, 1),
    ('6', 2, 2),
    ('-', 2, 3),
    ('1', 3, 0),
    ('2', 3, 1),
    ('3', 3, 2),
    ('*', 3, 3),
    ('0', 4, 0),
    ('C', 4, 1),
    ('=', 4, 2),
    ('/', 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=10, pady=10, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column)

clear_button = tk.Button(window, text='C', padx=10, pady=10, command=button_clear)
clear_button.grid(row=4, column=1)
equal_button = tk.Button(window, text='=', padx=10, pady=10, command=button_equal)
equal_button.grid(row=4, column=2)
window.mainloop()
