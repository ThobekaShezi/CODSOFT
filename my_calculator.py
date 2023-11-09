import tkinter as tk

# my function to perform  my arithmetic operations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to update the entry field when a button is clicked
def Update_after_button_click(value):
    current = entry.get()
    cursor_pos = entry.index(tk.INSERT)

    if value == 'C':
        entry.delete(0, tk.END)
    elif value == 'R':
        if cursor_pos > 0:
            entry.delete(cursor_pos - 1, cursor_pos)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, current[:cursor_pos] + value + current[cursor_pos:])

root = tk.Tk()
root.title("Thobeka's Calculator")

# Entry field for input and displaying results with background and foreground colors
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="lightgray", fg="black")
entry.grid(row=0, column=0, columnspan=4)

#create my buttons  
buttons = [
    '3', '4', '7', '/',
    '2', '5', '8', '*',
    '1', '6', '9', '+',
    '0', 'C', '=', '-',
    'R'
]

row_val = 1
col_val = 0

# Create buttons and assign them to the grid with colors
for button in buttons:
    if button == '=':
        action = calculate
    else:
        action = lambda x=button: Update_after_button_click(x)

    # adding different colors for my buttons
    if button.isdigit() or button in ['+', '-', '*', '/']:
        bg_color = "lightgrey"
        fg_color = "black"
    elif button == 'C':
        bg_color = "red"
        fg_color = "white"
    elif button == 'R':
        bg_color = "yellow"
        fg_color = "Black"
    else:
        bg_color = "lightgreen"
        fg_color = "black"
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 18), command=action, bg=bg_color, fg=fg_color).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
