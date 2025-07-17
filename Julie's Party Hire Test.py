import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#_______________________________________________________
# Function that handles login logic
def main():
    login()

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Hardcoded credentials
    username_correct = ""
    password_correct = ""

    # Check if credentials are correct
    if username == username_correct and password == password_correct:
        access_granted_window()
        main_button_window()
    else:
        access_denied_window()
    
# Function to close the main application window
def exit_program():
    root.destroy()

def logout():
    global root2
    root2.destroy()
    login_window()

# Function to show Access Granted window
def access_granted_window():
    messagebox.showinfo("Welcome","Credentials Correct!, Welcome Julie.")
    root.destroy()

def main_button_window():
    global root2
    root2 = tk.Tk()
    root2.title("Password Acceptance Screen")
    root2.geometry("600x500")
    root2.configure(bg="#c3ecfc")
    image = Image.open("C:/Users/22313/OneDrive - Lynfield College/2PAD/2PAD Assesements/91897 and 91896 Assessment (23rd July)/My Planning/Logo Concepts/ChatGPT Image May 16, 2025, 02_17_45 PM.png")
    resized_image = image.resize((300, 200))
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root2, image=photo)
    label.image = photo
    label.pack()
    btn_config = {"width": 12, "font": ("Times New Roman", 12)}
    tk.Button(root2, text="logout", command=logout, **btn_config, bg="red", fg="white").pack(pady=10)
    root2.mainloop()


# Function to show Access Denied window
def access_denied_window():
    messagebox.showerror("Login Failed", "Invalid Username or Password")

# Function to display login window (used for logout)
def login_window():
    global root, username_entry, password_entry
    root = tk.Tk()
    root.title("Password Entering Screen")
    root.geometry("600x350")
    root.configure(bg="#c3ecfc")
    
#_______________________________________________________
# Main Login Window
root = tk.Tk()
root.title("Password Entering Screen")
root.geometry("600x350")
root.configure(bg="#c3ecfc")

# Title label
title = tk.Label(root, text="Password Entering Screen", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
title.pack(pady=10)

# Frame to contain entry fields
frame = tk.Frame(root, bg="#c3ecfc")
frame.pack(pady=10)

# Labels and Entry widgets for Username and Password
labels = ["Username", "Password"]
entries = []
for label in labels:
    tk.Label(frame, text=label, font=("Times New Roman", 12), bg="#c3ecfc").pack(pady=3)
    entry = tk.Entry(frame, font=("Times New Roman", 12), width=30)
    entry.pack(pady=3)
    entries.append(entry)

# Unpack the entries into specific variables
username_entry, password_entry = entries

# Button Frame and buttons
button_frame = tk.Frame(root, bg="#c3ecfc")
button_frame.pack(pady=10)

btn_config = {"width": 12, "font": ("Times New Roman", 12)}
tk.Button(button_frame, text="Confirm", command=main, **btn_config ,bg="green", fg="#c3ecfc").grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Exit", command=exit_program, **btn_config, bg="red", fg="#c3ecfc").grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()
# Run the Tkinter main loop
login_window()
