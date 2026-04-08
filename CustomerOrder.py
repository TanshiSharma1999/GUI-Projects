import tkinter as tk

# Data (same as your tables)
customers = [
    {"id": 1, "name": "Rohan"},
    {"id": 2, "name": "Edward"},
    {"id": 3, "name": "Harry"},
    {"id": 4, "name": "Abriel"},
    

]

orders = [
    {"id": 1, "customerId": 3},
    {"id": 2, "customerId": 1},
    
]

# Function to find customers without orders
def get_customers_without_orders():
    order_ids = set()
    for order in orders:
        order_ids.add(order["customerId"])

    result = []
    for customer in customers:
        if customer["id"] not in order_ids:
            result.append(customer["name"])
    return result

# Function to display result in GUI
def show_customers():
    listbox.delete(0, tk.END)
    result = get_customers_without_orders()
    for name in result:
        listbox.insert(tk.END, name)

# Create window
root = tk.Tk()
root.title("Customer Finder")
root.geometry("300x300")

# Title label
label = tk.Label(root, text="Customers without Orders", font=("Arial", 14))
label.pack(pady=10)

# Listbox to display names
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

# Button
button = tk.Button(root, text="Find Customers", command=show_customers)
button.pack(pady=10)

# Run app
root.mainloop()
