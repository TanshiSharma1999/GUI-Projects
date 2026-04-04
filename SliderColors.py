import tkinter as tk

# Function to change background color
def change_color():
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()
    
    # Convert RGB to HEX
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    
    root.configure(bg=hex_color)
    color_label.config(text=f"Color: {hex_color}", bg=hex_color)

# Create main window
root = tk.Tk()
root.title("RGB Color Picker")
root.geometry("400x400")
root.configure(bg="#1e1e1e")  # Dark background

# Title label
title = tk.Label(root, text="RGB Color Picker", fg="white", bg="#1e1e1e", font=("Arial", 16))
title.pack(pady=10)

# Red slider
red_slider = tk.Scale(
    root, from_=0, to=255, orient="horizontal",
    label="Red", fg="white", bg="#1e1e1e",
    troughcolor="darkred", activebackground="red",
    highlightthickness=0
)
red_slider.pack(pady=10, fill="x", padx=20)

# Green slider
green_slider = tk.Scale(
    root, from_=0, to=255, orient="horizontal",
    label="Green", fg="white", bg="#1e1e1e",
    troughcolor="darkgreen", activebackground="green",
    highlightthickness=0
)
green_slider.pack(pady=10, fill="x", padx=20)

# Blue slider
blue_slider = tk.Scale(
    root, from_=0, to=255, orient="horizontal",
    label="Blue", fg="white", bg="#1e1e1e",
    troughcolor="darkblue", activebackground="blue",
    highlightthickness=0
)
blue_slider.pack(pady=10, fill="x", padx=20)

# Submit button
submit_btn = tk.Button(
    root, text="Apply Color",
    command=change_color,
    bg="#333333", fg="white",
    activebackground="#555555",
    relief="flat", padx=10, pady=5
)
submit_btn.pack(pady=20)

# Label to show hex color
color_label = tk.Label(root, text="Color: #000000", fg="white", bg="#1e1e1e")
color_label.pack(pady=10)

# Run app
root.mainloop()