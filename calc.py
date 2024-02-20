import tkinter as tk
from tkinter import font

def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#2b2b2b")

button_font = font.Font(family='Helvetica', size=12, weight='bold')

entry = tk.Entry(root, width=25, font=('Helvetica', 24), borderwidth=5, justify="right", bg="#2b2b2b", fg="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

button_bg = "#3c3f41"
button_active_bg = "#555555"
button_fg = "#ffffff"

buttons = [
    ("7", 1, 0, 1, 1), ("8", 1, 1, 1, 1), ("9", 1, 2, 1, 1), ("/", 1, 3, 1, 1),
    ("4", 2, 0, 1, 1), ("5", 2, 1, 1, 1), ("6", 2, 2, 1, 1), ("*", 2, 3, 1, 1),
    ("1", 3, 0, 1, 1), ("2", 3, 1, 1, 1), ("3", 3, 2, 1, 1), ("-", 3, 3, 1, 1),
    ("0", 4, 0, 1, 1), (".", 4, 1, 1, 1), ("C", 4, 2, 1, 1), ("+", 4, 3, 1, 1),
    ("=", 5, 0, 1, 4)
]

for (text, row, column, rowspan, columnspan) in buttons:
    button = tk.Button(root, text=text, padx=10, pady=5, font=button_font, bg=button_bg, activebackground=button_active_bg, fg=button_fg)
    button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5, sticky="ew")
    button.bind("<Button-1>", button_click)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
