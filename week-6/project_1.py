import tkinter as tk
from tkinter import messagebox

# This function runs when you click the "Check Price" button
def check_price():
    # Get the location and weight from the user inputs
    place = location_input.get().strip().lower()
    try:
        weight = float(weight_input.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a number for the weight.")
        return

    # Decide the amount based on the place and weight
    if place == "ibeju-lekki":
        if weight >= 10:
            cost = 5000
        else:
            cost = 3500
    elif place == "epe":
        if weight >= 10:
            cost = 10000
        else:
            cost = 5000
    else:
        messagebox.showerror("Error", "We don't deliver to that place.")
        return

    # Show the result
    result_label.config(text=f"Price: ₦{cost}")

# Set up the app window
window = tk.Tk()
window.title("Simi Services")
window.geometry("350x220")

# Ask for the location
tk.Label(window, text="Enter location:").pack(pady=5)
location_input = tk.Entry(window)
location_input.pack()

# Ask for the weight
tk.Label(window, text="Enter weight (kg):").pack(pady=5)
weight_input = tk.Entry(window)
weight_input.pack()

# Button to check the price
tk.Button(window, text="Check Price", command=check_price).pack(pady=10)

# Label to show the result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# Keep the window open
window.mainloop()
