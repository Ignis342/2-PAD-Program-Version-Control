#Luth Abdullah
#Date Started:
#Date Sumbitted:
# Necessary libraries for code to run
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

#Global Items
items = ["Tables", "Chairs", "Tents", "Linen", "Lights", "Speakers", "Heaters", "Fans", "Drink Glasses", "Cutlery", "Balloons", "Slushie Machine"]
item_prices = {"Tables": 10,"Chairs": 5,"Tents": 50,"Linen": 8,"Lights": 15,"Speakers": 30,"Heaters": 25,"Fans": 20,"Drink Glasses": 2,"Cutlery": 3,"Balloons": 1,"Slushie Machine": 60}
item_vars = {}
quantity_entries = {}

#_______________________________________________________
# Starts Code
def main():
    login()

#_______________________________________________________
# Login Screen
def login():
    username = username_entry.get()
    password = password_entry.get()

    #Username
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
# View records
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
# Add a new record
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
# Saves Current Order
def save_purchase():
    global item_prices
    recipet_number = generate_customer_id()
    customer_items = []
    item_number = 1
    total_price = 0

    for item in items:
        if item_vars[item].get():
            qty = quantity_entries[item].get()
            if qty.isdigit() and int(qty) > 0:
                qty_int = int(qty)
                price = item_prices.get(item, 0)
                item_total = qty_int * price
                total_price += item_total
                customer_items.append(
                    f"ID:{recipet_number} | Item No:{item_number} | {item} | Qty: {qty} | Price: ${item_total}"
                )
                item_number += 1

    if customer_items:
        try:
            with open("Reciepts.txt", "a") as file:
                for line in customer_items:
                    file.write(line + "\n")
                file.write("------------------------------------------------------------------------\n")
            messagebox.showinfo("Saved", f"Order saved for ID: {recipet_number}\nTotal: ${total_price}")
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
# Exit confirmation 
def ask_question():
    result = messagebox.askyesno("Exit Confirmation", "Are you sure you wish to close the program?")
    if result:
        root.destroy()

#_______________________________________________________
# logout button command
def logout():
    global root2
    root2.destroy()
    show_login_window()
#_______________________________________________________
# sucsessful login message
def show_access_granted_window():
    messagebox.showinfo("Welcome","Credentials Correct!, Welcome Julie.")
    root.withdraw()

#_______________________________________________________
# Delete all records button command
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
# Allows user to delete specific records
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

    receipt_viewer = tk.Button(root6, text="View Receipt", command=view_receipt, bg="pink", fg="white", font=("Times New Roman", 12)).pack(pady=5)
    delete_button = tk.Button(root6, text="Delete All Records", command=delete_records, bg="#FFA07A", fg="white", font=("Times New Roman", 12))
    delete_button.pack(pady=5)
    back_button = tk.Button(root6, text="Back", command=lambda: [root6.destroy(), main_button_window()], bg="red", fg="white", font=("Times New Roman", 12))
    back_button.pack(pady=10)
    root6.bind("<Escape>", lambda event: back_button.invoke())
    root6.bind("<BackSpace>", lambda event: delete_button.invoke())



#_______________________________________________________
# Main screen after successful login
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
# Item Hiring Window UI
def updated_equipment_hiring():
    close_window(root2)
    global root7

    root7 = tk.Toplevel()
    root7.title("Equipment Hiring")
    root7.state('zoomed')
    root7.configure(bg="#c3ecfc")

    title = tk.Label(root7, text="Equipment Hiring", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
    title.pack(pady=10)

    frame = tk.Frame(root7, bg="#c3ecfc")
    frame.pack(pady=10)

    header = tk.Frame(frame, bg="#c3ecfc")
    header.pack(anchor='w', pady=2)
    tk.Label(header, text="Item", font=("Arial", 11, "bold"), bg="#c3ecfc", width=20, anchor='w').grid(row=0, column=0, padx=1)
    tk.Label(header, text="Price ($)", font=("Arial", 11, "bold"), bg="#c3ecfc", width=10, anchor='w').grid(row=0, column=1, padx=1)
    tk.Label(header, text="Qty", font=("Arial", 11, "bold"), bg="#c3ecfc", width=5, anchor='w').grid(row=0, column=2, padx=1)

    for item in items:
        item_vars[item] = tk.IntVar()
        row = tk.Frame(frame, bg="#c3ecfc")
        row.pack(anchor='w', pady=2)

        tk.Checkbutton(row, text=item, variable=item_vars[item], bg="#c3ecfc",width=20, anchor='w').grid(row=0, column=0, padx=7)

        price_text = f"${item_prices.get(item, 0):.2f}"
        tk.Label(row, text=price_text, bg="#c3ecfc", width=10, anchor='w').grid(row=0, column=1, padx=7)

        quantity_entries[item] = tk.Entry(row, width=6)
        quantity_entries[item].grid(row=0, column=2, padx=7)

    btn_config = {"width": 20, "font": ("Times New Roman", 14)}
    tk.Button(root7, text="Currently Hired Equipment", command=view_records, **btn_config,
              bg="#FFD580", fg="white").pack(pady=10)
    save_button = tk.Button(root7, text="Place Order", command=save_purchase, **btn_config,
                            bg="#90EE90", fg="white")
    save_button.pack(pady=10)
    back_button = tk.Button(root7, text="Back", command=lambda: [root7.destroy(), main_button_window()],
                            bg="red", fg="white", font=("Times New Roman", 12))
    back_button.pack(pady=10)


    root7.bind("<Return>", lambda event: save_button.invoke())
    root7.bind("<Escape>", lambda event: back_button.invoke())
    
#_______________________________________________________
#Recipct Viewer UI
def view_receipt():
    global root8, receipt_entry, results_frame

    root8 = tk.Toplevel()
    root8.title("Receipt Viewer")
    root8.geometry("600x700")
    root8.configure(bg="#c3ecfc")

    title = tk.Label(root8, text="Receipt Viewer", font=("Times New Roman", 20, "bold"), bg="#c3ecfc", fg="#000000")
    title.pack(pady=10)

    # Entry for receipt number
    tk.Label(root8, text="Enter Receipt Number:", font=("Arial", 14), bg="#c3ecfc").pack(pady=5)
    receipt_entry = tk.Entry(root8, font=("Arial", 14), width=30)
    receipt_entry.pack(pady=5)

    # Confirm button
    confirm_button = tk.Button(root8, text="Confirm", font=("Times New Roman", 14), bg="#90EE90", fg="white", command=search_receipt)
    confirm_button.pack(pady=10)

    # Frame for displaying results
    results_frame = tk.Frame(root8, bg="#c3ecfc")
    results_frame.pack(pady=10)

    # Back button
    tk.Button(root8, text="Back", command=root8.destroy, bg="red", fg="white", font=("Times New Roman", 12)).pack(pady=10)

    root8.bind("<Return>", lambda event: confirm_button.invoke())

#_______________________________________________________
# Recipet printing screen
def search_receipt():
    receipt_num = receipt_entry.get().strip()

    # Clear previous search results
    for widget in results_frame.winfo_children():
        widget.destroy()

    if not receipt_num.isdigit():
        tk.Label(results_frame, text="Please enter a valid numeric receipt number.", font=("Arial", 14), bg="#c3ecfc", fg="red").pack()
        return

    try:
        with open("Reciepts.txt", "r") as file:
            lines = file.readlines()

        results = []
        total_price = 0

        for line in lines:
            if f"ID:{receipt_num}" in line:
                results.append(line.strip())

                # Extract item and quantity from line
                try:
                    parts = line.split("|")
                    item_part = parts[2].strip()   # item name
                    qty_part = parts[3].strip()    # Qty: N
                    item_name = item_part
                    qty = int(qty_part.replace("Qty:", "").strip())
                    price = item_prices.get(item_name, 0)
                    total_price += qty * price
                except:
                    pass  # skip malformed lines

        if results:
            for res in results:
                tk.Label(results_frame, text=res, font=("Arial", 14), bg="#c3ecfc", anchor="w", justify="left").pack(anchor="w")
            # Show total
            tk.Label(results_frame, text=f"Total Price: ${total_price:.2f}", font=("Arial", 16, "bold"), bg="#c3ecfc", fg="green").pack(pady=10)
        else:
            tk.Label(results_frame, text=f"No records found for Receipt ID: {receipt_num}", font=("Arial", 14), bg="#c3ecfc", fg="red").pack()

    except FileNotFoundError:
        tk.Label(results_frame, text="Records file not found.", font=("Arial", 14), bg="#c3ecfc", fg="red").pack()

#_______________________________________________________
def print_receipt():
    receipt_num = receipt_entry.get().strip()
    if not receipt_num.isdigit():
        messagebox.showwarning("Warning", "Please enter a valid numeric receipt number.")
        return

    try:
        with open("Reciepts.txt", "r") as file:
            lines = file.readlines()

        results = []
        total_price = 0

        for line in lines:
            if f"ID:{receipt_num}" in line:
                results.append(line.strip())

                try:
                    parts = line.split("|")
                    item_part = parts[2].strip()   # item name
                    qty_part = parts[3].strip()    # Qty: N
                    item_name = item_part
                    qty = int(qty_part.replace("Qty:", "").strip())
                    price = item_prices.get(item_name, 0)
                    total_price += qty * price
                except:
                    pass  # skip malformed lines

        if results:
            # Write to temporary file
            filename = f"Receipt_{receipt_num}.txt"
            with open(filename, "w") as f:
                f.write("Receipt Details:\n")
                f.write("---------------------------\n")
                for res in results:
                    f.write(res + "\n")
                f.write(f"\nTotal Price: ${total_price:.2f}\n")
            os.startfile(filename, "print")  # Windows only
        else:
            messagebox.showinfo("Info", f"No records found for Receipt ID: {receipt_num}")

    except FileNotFoundError:
        messagebox.showerror("Error", "Records file not found.")



# Launch the login screen on start
used_ids = set()
show_login_window()
