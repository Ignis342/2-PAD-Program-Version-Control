# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

#_______________________________________________________
# Entry point of the program
def main():
    login()

#_______________________________________________________
# Handles login verification
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Hardcoded credentials (currently empty)
    username_correct = ""
    password_correct = ""


    # Check credentials
    if username == username_correct and password == password_correct:
        show_access_granted_window()
        main_button_window()
    else:
        show_access_denied_window()


#_______________________________________________________
# Allows user to go back to main screen
def close_window(window):
    window.destroy()
    
    
#_______________________________________________________
# View stored student records
def view_records():
    view_window = tk.Toplevel()
    view_window.title("Hired Equipment")
    view_window.state('zoomed')
    try:
        with open("Reciepts.txt", "r") as file:
            records = file.readlines()
        text = "\n".join(records) if records else "No records found."
    except FileNotFoundError:
        text = "No records found."
    
    records_label = tk.Label(view_window, text=text, justify="left", font=("Arial", 12))
    records_label.pack(padx=10, pady=10)

#_______________________________________________________
# Add a new record to the file
def add_record():
    global roll_entry, recipet_number
    recipet_number = random.randrange(1000, 9999)
    selected_equipment = equipment_combo.get()
    quantity = roll_entry.get()

    if quantity and selected_equipment:
        with open("Reciepts.txt", "a") as file:
            file.write(f"{recipet_number},{selected_equipment},{quantity}\n")
        roll_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Order placed!\nReceipt Number: {recipet_number}")
    else:
        messagebox.showwarning("Warning", "Enter quantity.")

#_______________________________________________________
# Add a new record to the file
def save_purchase():
    recipet_number = generate_customer_id()
    customer_items = []
    item_number = 1
    for item in items:
        if item_vars[item].get():
            qty = quantity_entries[item].get()
            if qty.isdigit() and int(qty) > 0:
                customer_items.append(f"ID:{recipet_number} | Item No:{item_number} | {item} | Qty: {qty}")
                item_number += 1

    if customer_items:
        try:
            with open("Reciepts.txt", "a") as file:
                for line in customer_items:
                    file.write(line + "\n")
            messagebox.showinfo("Saved", f"Data saved for Customer ID: {recipet_number}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
    else:
        messagebox.showerror("Input Error", "Please select at least one item with quantity.")

#_______________________________________________________
# Generates customer ID
def generate_customer_id():
    while True:
        new_id = random.randint(1000, 9999)
        if new_id not in used_ids:
            used_ids.add(new_id)
            return new_id
#_______________________________________________________
# Exit confirmation dialog
def ask_question():
    result = messagebox.askyesno("Exit Confirmation", "Are you sure you wish to close the program?")
    if result:
        root.withdraw()

#_______________________________________________________
# Handle logout functionality
def logout():
    global root2
    root2.destroy()
    show_login_window()
#_______________________________________________________
# Show success message for login
def show_access_granted_window():
    messagebox.showinfo("Welcome","Credentials Correct!, Welcome Julie.")
    root.withdraw()

#_______________________________________________________
# Allows user to delete records
def delete_records():
    try:
        with open("Reciepts.txt", "w") as file:
            pass
        text_widget.config(state=tk.NORMAL)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "All records deleted.")
        text_widget.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete records: {str(e)}")
#_______________________________________________________
# Allows user to delete records
def delete_information():
    receipt_number = delete_entry.get().strip()
    item_number = delete_item.get().strip()

    if not receipt_number:
        messagebox.showwarning("Warning", "Please enter a receipt number.")
        return

    try:
        with open("Reciepts.txt", "r") as file:
            records = file.readlines()

        new_records = []
        found = False

        for record in records:
            if f"ID:{receipt_number}" in record:
                if item_number and f"Item No:{item_number}" in record:
                    found = True
                    continue  
                elif not item_number:
                    found = True
                    continue  
            new_records.append(record)

        with open("Reciepts.txt", "w") as file:
            file.writelines(new_records)

        if found:
            msg = f"Deleted {'item' if item_number else 'receipt'} successfully."
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showwarning("Warning", "Record not found.")

        delete_entry.delete(0, tk.END)
        delete_item.delete(0, tk.END)

    except FileNotFoundError:
        messagebox.showerror("Error", "Records file not found.")
#_______________________________________________________
# Equipment Hiring window UI
#def equipment_hiring(): (Obsolete)
    close_window(root2)
    global root4, quantity_entry, roll_entry, equipment_combo

    root4 = tk.Toplevel()

    root4.title("Equipment Hiring")
    root4.state('zoomed')
    root4.configure(bg="#c3ecfc")

    title = tk.Label(root4, text="Equipment Hiring", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
    title.pack(pady=10)

    btn_config = {"width": 20, "font": ("Times New Roman", 14)}

    # Dropdown for item selection
    tk.Label(root4, text="Item Hired:", font=("Times New Roman", 12), bg="#c3ecfc").pack(pady=5)
    equipment_options = ["Tables", "Chairs", "Tents", "Linen", "Lights","Speakers","Heaters","Fans","Drink Glasses","Cutlery","Balloons","Slushie Machine","Party Games(Choose 5)"]
    equipment_combo = ttk.Combobox(root4, values=equipment_options, font=("Times New Roman", 12))
    equipment_combo.pack(pady=5)
    equipment_combo.current(0)


    # Quantity entry
    tk.Label(root4, text="Item Quantity", font=("Arial", 12), bg="#c3ecfc").pack(pady=10)
    roll_entry = tk.Entry(root4, font=("Arial", 12), width=30)
    roll_entry.pack(pady=3)

    # Buttons
    tk.Button(root4, text="Currently Hired Equipment", command=view_records, **btn_config, bg="#FFD580", fg="white").pack(pady=10)
    tk.Button(root4, text="Place Order", command=add_record, **btn_config, bg="#90EE90", fg="white").pack(pady=10)
    tk.Button(root4, text="Back", command=lambda: [root4.destroy(), main_button_window()],bg="red", fg="white", font=("Times New Roman", 12)).pack(pady=10)

#_______________________________________________________
# Equipment Return window UI
def equipment_return():
    close_window(root2)
    global root5, delete_entry, delete_item

    root5 = tk.Toplevel()
    root5.title("Equipment Return")
    root5.state('zoomed')
    root5.configure(bg="#c3ecfc")

    title = tk.Label(root5, text="Equipment Return", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
    title.pack(pady=10)

    btn_config = {"width": 20, "font": ("Times New Roman", 14)}

    tk.Label(root5, text="Enter Receipt Number to Delete:", font=("Arial", 12), bg="#c3ecfc").pack(pady=10)
    delete_entry = tk.Entry(root5, font=("Arial", 12), width=30)
    delete_entry.pack(pady=5)
    

    tk.Label(root5, text="Enter Item Number to Delete:", font=("Arial", 12), bg="#c3ecfc").pack(pady=10)
    delete_item = tk.Entry(root5, font=("Arial", 12), width=30)
    delete_item.pack(pady=5)

    tk.Button(root5, text="Currently Hired Equipment", command=view_records, **btn_config, bg="#FFD580", fg="white").pack(pady=10)
    submit_button = tk.Button(root5, text="Submit Return", command=delete_information, **btn_config, bg="#90EE90", fg="white")
    submit_button.pack(pady=10)
    back_button = tk.Button(root5, text="Back", command=lambda: [root5.destroy(), main_button_window()], bg="red", fg="white", font=("Times New Roman", 12))
    back_button.pack(pady=10)
    root5.bind("<Escape>", lambda event: back_button.invoke())
    root5.bind("<Return>", lambda event: submit_button.invoke())

#_______________________________________________________
# Currently Hired Equipment window UI
def currently_hired_equipment():
    close_window(root2)
    global root6, text_widget

    root6 = tk.Toplevel()

    root6.title("Currently Hired Equipment")
    root6.state('zoomed')
    root6.configure(bg="#c3ecfc")

    title = tk.Label(root6, text="Currently Hired Equipment", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
    title.pack(pady=10)

    frame = tk.Frame(root6)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Arial", 12))
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=text_widget.yview)

    try:
        with open("Reciepts.txt", "r") as file:
            records = file.readlines()
        text = "".join(records) if records else "No records found."
    except FileNotFoundError:
        text = "No records found."

    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)

    delete_button = tk.Button(root6, text="Delete All Records", command=delete_records, bg="#FFA07A", fg="white", font=("Times New Roman", 12))
    delete_button.pack(pady=5)
    back_button = tk.Button(root6, text="Back", command=lambda: [root6.destroy(), main_button_window()], bg="red", fg="white", font=("Times New Roman", 12))
    back_button.pack(pady=10)
    root6.bind("<Escape>", lambda event: back_button.invoke())
    root6.bind("<BackSpace>", lambda event: delete_button.invoke())



#_______________________________________________________
# Main Dashboard after successful login
def main_button_window():
    global root2, photo

    root2 = tk.Toplevel()
    root2.title("Julie's Party Hire")
    root2.state('zoomed')
    root2.configure(bg="#c3ecfc")

    # Display logo/image
    image = Image.open("C:/Users/22313/OneDrive - Lynfield College/2PAD/2PAD Assesements/91897 and 91896 Assessment (23rd July)/My Planning/Logo Concepts/ChatGPT Image May 16, 2025, 02_17_45 PM.png")
    resized_image = image.resize((300, 200))
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root2, image=photo, bg="#c3ecfc")
    label.pack()

    btn_config = {"width": 20, "font": ("Times New Roman", 14)}

    # Dashboard buttons
    tk.Button(root2, text="Equipment Hiring", command=updated_equipment_hiring, **btn_config, bg="#ADD8E6", fg="white").pack(pady=10)
    tk.Button(root2, text="Equipment Return", command=equipment_return, **btn_config, bg="#ADD8E6", fg="white").pack(pady=10)
    tk.Button(root2, text="Currently Hired Equipment", command=currently_hired_equipment, **btn_config, bg="#ADD8E6", fg="white").pack(pady=10)
    logout_button = tk.Button(root2, text="Logout", command=logout, **btn_config, bg="red", fg="white")
    logout_button.pack(pady=10)
    root2.bind("<Escape>", lambda event: logout_button.invoke())


    root2.mainloop()

#_______________________________________________________
# Show error if login fails
def show_access_denied_window():
    messagebox.showerror("Login Failed", "Invalid Username or Password")

#_______________________________________________________
# Login Window UI
def show_login_window():
    global root, username_entry, password_entry
    root = tk.Tk()
    root.title("Login Screen")
    root.state('zoomed')
    root.configure(bg="#c3ecfc")

    # Title
    title = tk.Label(root, text="Password Entering Screen", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
    title.pack(pady=10)

    # Entry form for username/password
    frame = tk.Frame(root, bg="#c3ecfc")
    frame.pack(pady=10)

    labels = ["Username", "Password"]
    entries = []
    for label in labels:
        tk.Label(frame, text=label, font=("Times New Roman", 12), bg="#c3ecfc").pack(pady=3)
        entry = tk.Entry(frame, font=("Times New Roman", 12), width=30, show="*" if label == "Password" else "")
        entry.pack(pady=3)
        entries.append(entry)

    username_entry, password_entry = entries

    # Buttons
    button_frame = tk.Frame(root, bg="#c3ecfc")
    button_frame.pack(pady=10)

    btn_config = {"width": 12, "font": ("Times New Roman", 12)}
    confirm_button= tk.Button(button_frame, text="Confirm", command=main, **btn_config ,bg="green", fg="white")
    confirm_button.pack(pady=10)
    logout_button = tk.Button(button_frame, text="Exit", command=ask_question, **btn_config, bg="red", fg="white")
    logout_button.pack(pady=10)
    root.bind("<Return>", lambda event: confirm_button.invoke())
    root.bind("<Escape>", lambda event: logout_button.invoke())

    root.mainloop()
    
#_______________________________________________________
# Test Root
def updated_equipment_hiring():
    close_window(root2)
    global root7, item_vars, quantity_entries, items

    root7 = tk.Toplevel()
    root7.title("Equipment Hiring")
    root7.state('zoomed')
    root7.configure(bg="#c3ecfc")

    title = tk.Label(root7, text="Equipment Hiring", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
    title.pack(pady=10)

    items = ["Tables", "Chairs", "Tents", "Linen", "Lights","Speakers","Heaters","Fans","Drink Glasses","Cutlery","Balloons","Slushie Machine"]
    item_vars = {}
    quantity_entries = {}

    frame = tk.Frame(root7, bg="#c3ecfc")
    frame.pack(pady=10)

    tk.Label(frame, text="Item", font=("Arial", 11, "bold"), bg="#c3ecfc").grid(row=0, column=0, padx=5)
    tk.Label(frame, text="Qty", font=("Arial", 11, "bold"), bg="#c3ecfc").grid(row=0, column=1, padx=5)

    for i, item in enumerate(items):
        item_vars[item] = tk.IntVar()
        tk.Checkbutton(frame, text=item, variable=item_vars[item], bg="#c3ecfc").grid(row=i+1, column=0, sticky=tk.W, padx=10, pady=2)
        quantity_entries[item] = tk.Entry(frame, width=5)
        quantity_entries[item].grid(row=i+1, column=1, pady=2)

    btn_config = {"width": 20, "font": ("Times New Roman", 14)}
    
    tk.Button(root7, text="Currently Hired Equipment", command=view_records,**btn_config, bg="#FFD580", fg="white").pack(pady=10)
    save_button = tk.Button(root7, text="Place Order", command=save_purchase, **btn_config, bg="#90EE90", fg="white")
    save_button.pack(pady=10) 
    back_button = tk.Button(root7, text="Back", command=lambda: [root7.destroy(), main_button_window()], bg="red", fg="white", font=("Times New Roman", 12))
    back_button.pack(pady=10)
    root7.bind("<Return>", lambda event: save_button.invoke())
    root7.bind("<Escape>", lambda event: back_button.invoke())

    
#_______________________________________________________
# Launch the login screen on start
used_ids = set()
show_login_window()
