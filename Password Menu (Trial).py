import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Not used currently, but useful for future image handling

#_______________________________________________________
# Function that handles login logic
def main():
    username = username_entry.get()
    password = password_entry.get()

    # Hardcoded credentials
    username_correct = "Julie1998"
    password_correct = "PartyForLife"

    # Check if credentials are correct
    if username == username_correct and password == password_correct:
        # Access Granted Window
        root2 = tk.Tk()
        root2.title("Password Acceptance Screen")
        root2.geometry("600x500")
        tk.Label(root2, text="Access Granted!", font=("Times New Roman", 20), fg="green").pack(pady=20)
        tk.Button(root2, text="Exit", command=root2.destroy, bg="red", fg="white", font=("Times New Roman", 12)).pack(pady=10)
    else:
        # Access Denied Window
        root3 = tk.Tk()
        root3.title("Incorrect Password Screen")
        root3.geometry("600x500")
        tk.Label(root3, text="Access Denied!", font=("Times New Roman", 20), fg="red").pack(pady=20)
        tk.Button(root3, text="Exit", command=root3.destroy, bg="red", fg="white", font=("Times New Roman", 12)).pack(pady=10)

# Function to close the main application window
def exit_program():
    root.destroy()

#_______________________________________________________
# Main Login Window
root = tk.Tk()
root.title("Password Entering Screen")
root.geometry("600x500")
root.configure(bg="#CFE4FF")

# Title label
title = tk.Label(root, text="Password Entering Screen", font=("Times New Roman", 20, "bold"), bg="#CFE4FF", fg="#000000")
title.pack(pady=10)

# Frame to contain entry fields
frame = tk.Frame(root, bg="#CFE4FF")
frame.pack(pady=10)

# Labels and Entry widgets for Username and Password
labels = ["Username", "Password"]
entries = []
for label in labels:
    tk.Label(frame, text=label, font=("Times New Roman", 12), bg="#CFE4FF").pack(pady=3)
    entry = tk.Entry(frame, font=("Times New Roman", 12), width=30)
    entry.pack(pady=3)
    entries.append(entry)

# Unpack the entries into specific variables
username_entry, password_entry = entries

# Button Frame and buttons
button_frame = tk.Frame(root, bg="#CFE4FF")
button_frame.pack(pady=10)

btn_config = {"width": 12, "font": ("Times New Roman", 12)}
tk.Button(button_frame, text="Confirm", command=main, **btn_config ,bg="green", fg="#CFE4FF").grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Exit", command=exit_program, **btn_config, bg="red", fg="#CFE4FF").grid(row=2, column=0, columnspan=2, pady=5)

# Run the Tkinter main loop
root.mainloop()
