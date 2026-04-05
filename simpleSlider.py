import tkinter as tk

def update_value(val):
    number_label.config(text=f"Value: {val}")

root = tk.Tk()
root.title("Slider Demo")
root.geometry("300x200")

# Slider
slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    command=update_value
)
slider.pack(pady=20)

# Label to show value
number_label = tk.Label(root, text="Value: 0", font=("Arial", 14))
number_label.pack()

root.mainloop()