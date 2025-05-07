import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def add_record():
    roll_no = roll_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    class_ = class_entry.get()
    if roll_no and name:
        with open("students.txt", "a") as file:
            file.write(f"{roll_no},{name},{age},{gender},{class_}\n")
        roll_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        class_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Record added successfully.")
    else:
        messagebox.showwarning("Warning", "Enter Roll No, Name, Age, Gender and Class")

def delete_record():
    roll_no = roll_entry.get()
    if roll_no:
        records = []
        found = False
        with open("students.txt", "r") as file:
            records = file.readlines()
        with open("students.txt", "w") as file:
            for record in records:
                if not record.startswith(roll_no + ","):
                    file.write(record)
                else:
                    found = True
        if found:
            messagebox.showinfo("Success", "Record deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Record not found.")
        roll_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter Roll No")

def view_records():
    view_window = tk.Toplevel(root)
    view_window.title("Student Records")
    view_window.geometry("400x300")
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()
        if records:
            text = "\n".join(records)
        else:
            text = "No records found."
    except FileNotFoundError:
        text = "No records found."
    records_label = tk.Label(view_window, text=text, justify="left", font=("Arial", 12))
    records_label.pack(padx=10, pady=10)

def clear_records():
    with open("students.txt", "w") as file:
        file.truncate()
    messagebox.showinfo("Success", "All records cleared.")

def exit_program():
    root.destroy()

# Create window
root = tk.Tk()
root.title("Students Data Management System")
root.geometry("600x500")

# Load background image
#bg_image = Image.open("C:/Users/22313/OneDrive - Lynfield College/2PAD/2PAD tasks/60th Reunion Website Banner.jpg")
#bg_image = bg_image.resize((1920, 1080), Image.LANCZOS) 
#bg_photo = ImageTk.PhotoImage(bg_image)

# Display background
#bg_label = tk.Label(root, image=bg_photo)
#bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title = tk.Label(root, text="Student Data Management", font=("Arial", 20, "bold"), bg="#ffffff", fg="#000000")
title.pack(pady=10)

# Form fields
frame = tk.Frame(root, bg="#ffffff")
frame.pack(pady=10)

labels = ["Roll No", "Name", "Age", "Gender", "Class"]
entries = []
for label in labels:
    tk.Label(frame, text=label, font=("Arial", 12), bg="#ffffff").pack(pady=3)
    entry = tk.Entry(frame, font=("Arial", 12), width=30)
    entry.pack(pady=3)
    entries.append(entry)

roll_entry, name_entry, age_entry, gender_entry, class_entry = entries

# Buttons
button_frame = tk.Frame(root, bg="#ffffff")
button_frame.pack(pady=10)

btn_config = {"width": 12, "font": ("Arial", 12), "bg": "#4CAF50", "fg": "white", "activebackground": "#45a049"}
tk.Button(button_frame, text="Add", command=add_record, **btn_config).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Delete", command=delete_record, **btn_config).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="View", command=view_records, **btn_config).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Clear", command=clear_records, **btn_config).grid(row=1, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Exit", command=exit_program, **btn_config).grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()
