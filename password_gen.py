import random
import string
import tkinter as tk
from tkinter import Entry, Label, Button

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        len = int(length_entry.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.", fg="red")
        return

    if len <= 0:
        result_label.config(text="Password length should be greater than 0.", fg="red")
        return
    
    elif len >= 20:
        result_label.config(text="Password length should be less than 20.", fg="red")
        return

    user_password = generate_password(len)
    result_label.config(text="Generated Password: " + user_password, fg="black")


app = tk.Tk()
app.title("Thobeka's Password Generator")


length_label = Label(app, text="Enter the desired length of the password:", fg="black")
length_label.pack(pady=10)

length_entry = Entry(app)
length_entry.pack(pady=10)

generate_button = Button(app, text="Generate Password", command=generate_and_display_password, bg="lightblue")
generate_button.pack(pady=20)

result_label = Label(app, text="", fg="black")
result_label.pack()


app.mainloop()
