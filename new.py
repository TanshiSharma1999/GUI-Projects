import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("Cool Tkinter App")
root.geometry("300x200")
root.configure(bg="black")

# Function to change color
def change_color():
    colors = ["#ff4d4d", "#4dff4d", "#4d4dff", "#ffff4d", "#ff4dff", "#4dffff"]
    new_color = random.choice(colors)
    button.config(bg=new_color, activebackground=new_color)
    label.config(text="Color Changed!", fg=new_color)

# Label
label = tk.Label(root, text="Click the button!", bg="black", fg="white", font=("Arial", 12))
label.pack(pady=20)

# Button
button = tk.Button(root, text="Click Me", command=change_color,
                   bg="white", fg="black", font=("Arial", 12), padx=10, pady=5)
button.pack()

# Run app
root.mainloop()