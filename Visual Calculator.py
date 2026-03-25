import tkinter as tk

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Window
root = tk.Tk()
root.title("Tanshi's Calculator")
root.geometry("300x400")
root.configure(bg="black")   # 🔥 black background

# Entry box
entry = tk.Entry(
    root,
    font=("Arial", 20),
    bd=5,
    relief=tk.RIDGE,
    justify="right",
    bg="black",        # black background
    fg="white",        # white text
    insertbackground="white"  # cursor color
)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root, bg="black")
frame.pack()

row = 0
col = 0

for button in buttons:
    action = lambda x=button: calculate() if x == '=' else click(x)
    
    tk.Button(
        frame,
        text=button,
        width=5,
        height=2,
        font=("Arial", 14),
        bg="black",     # button bg
        fg="white",     # text color
        activebackground="gray",
        activeforeground="white",
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 14),
    bg="black",
    fg="white",
    activebackground="gray",
    command=clear
).pack(fill=tk.BOTH, padx=10, pady=5)

root.mainloop()