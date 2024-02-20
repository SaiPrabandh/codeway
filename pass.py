import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_scale.get()

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.config(text=password)
root = tk.Tk()
root.title("Password Generator")
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()
length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)
complexity_label = tk.Label(frame, text="Password Complexity:")
complexity_label.grid(row=1, column=0, padx=5, pady=5)

complexity_scale = tk.Scale(frame, from_=1, to=3, orient=tk.HORIZONTAL, resolution=1)
complexity_scale.grid(row=1, column=1, padx=5, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

password_display = tk.Label(root, text="", font=("Helvetica", 14), padx=10, pady=10)
password_display.pack()

root.mainloop()
