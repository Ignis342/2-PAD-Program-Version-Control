import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Not used currently, but useful for future image handling

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
        show_access_granted_window()
        main_button_window()
    else:
        show_access_denied_window()
    

# Function to close the main application window
def ask_question():
    result = messagebox.askyesno("Exit Confirmation", "Are you sure you wish to close the program?")
    if result:
        root.destroy()

def logout():
    global root2
    root2.destroy()
    show_login_window()

# Function to show Access Granted window
def show_access_granted_window():
    messagebox.showinfo("Welcome","Credentials Correct!, Welcome Julie.")
    root.destroy()

def equipment_hiring():
    global root4
    root4 = tk.Tk()
    root4.title("Password Acceptance Screen")
    root4.geometry("600x500")
    tk.Label(root4, text="equipment_hiring!", font=("Times New Roman", 20), fg="green").pack(pady=20)
    tk.Button(root4, text="Exit", command=root4.destroy, bg="red", fg="white", font=("Times New Roman", 12)).pack(pady=10)

def equipment_return():
    global root5
    root5 = tk.Tk()
    root5.title("Password Acceptance Screen")
    root5.geometry("600x500")
    tk.Label(root5, text="equipment_return!", font=("Times New Roman", 20), fg="green").pack(pady=20)
    tk.Button(root5, text="Exit", command=root5.destroy, bg="red", fg="white", font=("Times New Roman", 12)).pack(pady=10)

def currently_hired_equipment():
    global root6
    root6 = tk.Tk()
    root6.title("Password Acceptance Screen")
    root6.geometry("600x500")
    tk.Label(root6, text="currently_hired_equipment!", font=("Times New Roman", 20), fg="green").pack(pady=20)
    tk.Button(root6, text="Exit", command=root6.destroy, bg="red", fg="white", font=("Times New Roman", 12)).pack(pady=10)

def main_button_window():
    global root2
    root2 = tk.Tk()
    root2.title("Julie's Party Hire")
    root2.geometry("600x500")
    root2.configure(bg="#c3ecfc")
    image = Image.open("C:/Users/22313/OneDrive - Lynfield College/2PAD/2PAD Assesements/91897 and 91896 Assessment (23rd July)/My Planning/Logo Concepts/ChatGPT Image May 16, 2025, 02_17_45 PM.png")
    resized_image = image.resize((300, 200))
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root2, image=photo)
    label.image = photo
    label.pack()
    btn_config = {"width": 20, "font": ("Times New Roman", 14)}
    tk.Button(root2, text="Equipment Hiring", command=equipment_hiring, **btn_config, bg="#ADD8E6", fg="white").pack(pady=10)
    btn_config = {"width": 20, "font": ("Times New Roman", 14)}
    tk.Button(root2, text="Equipment Return", command=equipment_return, **btn_config, bg="#ADD8E6", fg="white").pack(pady=10)
    btn_config = {"width": 20, "font": ("Times New Roman", 14)}
    tk.Button(root2, text="Currently Hired Equipment", command=currently_hired_equipment, **btn_config, bg="#ADD8E6", fg="white").pack(pady=10)
    btn_config = {"width": 20, "font": ("Times New Roman", 14)}
    tk.Button(root2, text="logout", command=logout, **btn_config, bg="red", fg="white").pack(pady=10)
    root2.mainloop()

# Function to show Access Denied window
def show_access_denied_window():
    messagebox.showerror("Login Failed", "Invalid Username or Password")

# Function to display login window (used for logout)
def show_login_window():
    global root, username_entry, password_entry
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
        entry = tk.Entry(frame, font=("Times New Roman", 12), width=30, show="*" if label == "Password" else "")
        entry.pack(pady=3)
        entries.append(entry)

    # Unpack the entries into specific variables
    username_entry, password_entry = entries

    # Button Frame and buttons
    button_frame = tk.Frame(root, bg="#c3ecfc")
    button_frame.pack(pady=10)

    btn_config = {"width": 12, "font": ("Times New Roman", 12)}
    tk.Button(button_frame, text="Confirm", command=main, **btn_config ,bg="green", fg="#c3ecfc").grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Exit", command=ask_question, **btn_config, bg="red", fg="#c3ecfc").grid(row=2, column=0, columnspan=2, pady=5)

    root.mainloop()

# Initial call to display the login window
show_login_window()
