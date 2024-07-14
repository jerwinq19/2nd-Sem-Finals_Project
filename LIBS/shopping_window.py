from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import datetime, os, json

def main_shop(win):
    win.withdraw()
    root = ctk.CTkToplevel()
    root.title("Shop-IT")
    app_width, app_height = 1400, 900
    root.resizable(False, False)

    def show_frame(frames):
        frames.tkraise()
        
    def image_loader(path: str) -> ctk.CTkImage:
        test = Image.open(path)
        image = ctk.CTkImage(light_image=test, size=(250, 230))
        return image

    screen_height, screen_width = root.winfo_screenheight(), root.winfo_screenwidth()

    x_cord, y_cord = (screen_width / 2) - (app_width / 2), (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x_cord)}+{int(y_cord)}")

    # Frames
    top_frame = ctk.CTkFrame(root, width=1400, height=80, fg_color="#f2f2f2", corner_radius=1)
    top_frame.pack(side=TOP)

    mid_frame = ctk.CTkFrame(root, width=1400, height=900, fg_color="#e0e0e0", corner_radius=1)
    mid_frame.pack()

    shop_frame = ctk.CTkFrame(mid_frame, width=1400, height=900, fg_color="#e0e0e0", corner_radius=1)
    shop_frame.place(x=0,y=0)
    shop_frame.grid_propagate(False)

    cart_frame = ctk.CTkFrame(mid_frame, width=1400, height=900, fg_color="#e0e0e0", corner_radius=1)
    cart_frame.place(x=0,y=0)

    accounts_frame = ctk.CTkFrame(mid_frame, width=1400, height=900, fg_color="#e0e0e0", corner_radius=1)
    accounts_frame.place(x=0,y=0)
    
    
    ctk.CTkLabel(top_frame, text="Shop-IT", font=("Serif", 32, "bold"), text_color="#379777", anchor=CENTER).place(x=100, y=20)
    top_btn_font = ("Serif",20, "bold")

    image_path = [
        "ASSETS/Account.png",
        "ASSETS/Cart.png",
        "ASSETS/Shop.png"
    ]
    def image_loader_2(path, size1, size2):
        test = Image.open(path)
        image = ctk.CTkImage(light_image=test, size=(size1, size2))
        return image

    account_img = image_loader_2(image_path[0], 50, 50)
    cart_img = image_loader_2(image_path[1], 50,50)
    shop_img = image_loader_2(image_path[2], 50,50)



    comp_btn = ctk.CTkButton(top_frame, text="Shop", font=top_btn_font, fg_color="#f2f2f2",anchor=CENTER, text_color="#000000",command=lambda:show_frame(shop_frame), image=shop_img, compound=RIGHT)
    comp_btn.place(x=300, y=10)

    cart_btn = ctk.CTkButton(top_frame, text="Cart", font=top_btn_font, fg_color="#f2f2f2", anchor=CENTER, text_color="#000000",command=lambda:show_frame(cart_frame), image=cart_img, compound=RIGHT)
    cart_btn.place(x=500, y=10)
    
    account_btn = ctk.CTkButton(top_frame, text="Account", font=top_btn_font, fg_color="#f2f2f2", anchor=CENTER, text_color="#000000",command=lambda:show_frame(accounts_frame), image=account_img, compound=RIGHT)
    account_btn.place(x=1200, y=10)

    scrollable_shop = ctk.CTkScrollableFrame(shop_frame, width=1340, height=750, fg_color="#e0e0e0")
    scrollable_shop.place(x=20,y=50)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------ #    
    
    Account_details_frame = ctk.CTkFrame(accounts_frame, width=1370, height=300, border_color="#000000", border_width=2, fg_color="#f2f2f2")
    Account_details_frame.place(x=15,y=30)
    
    image_lbl = ctk.CTkLabel(Account_details_frame, width=200, height=200, fg_color="#e2e2e2", text_color="#000000", text="")
    image_lbl.place(x=30,y=50)
    
    accounts_name = ctk.CTkLabel(Account_details_frame, text="Username:", font=("Serif", 30,"bold"), text_color="#000000", fg_color="transparent")
    accounts_name.place(x=250,y=50)
    
    member_type_lbl = ctk.CTkLabel(Account_details_frame, text="Member Type:", font=("Serif", 30,"bold"), text_color="#000000", fg_color="transparent")
    member_type_lbl.place(x=250,y=100)
    
    total_order_lbl = ctk.CTkLabel(Account_details_frame, text="Total Orders:", font=("Serif", 30,"bold"), text_color="#000000", fg_color="transparent")
    total_order_lbl.place(x=250,y=150)
    
    def change_accounts_details():
        global user_name
        with open('CREDS/user_creds.json', 'r') as login_file:
            # Load JSON data from the file
            login_details = json.load(login_file)

        for each_logged in login_details["user_credentials"]:
            if each_logged.get("is_logged_in", True): # check if true 
                pfp_image = image_loader_2(each_logged["Profile_path"], 200, 200)
                image_lbl.configure(image=pfp_image)
                user_name = each_logged["User_name"]
                member_type = each_logged["User_type"]
                total_order_sum = each_logged["Total_Orders"]
                print(total_order_sum)
            
                accounts_name.configure(text=f"Username: {user_name}")
                member_type_lbl.configure(text=f"Member type: {member_type}")
                total_order_lbl.configure(text=f"Total orders: {total_order_sum}")
                
    # ------------------------------------------------------------------------------------------------------------------------------------------------------ #
    cart_title = ctk.CTkLabel(cart_frame, text="Your Cart", font=("Serif", 32, "bold"), text_color="#379777").place(x=30, y=30)

    columns = ("#", "Item name", "Quantity", "Price", "Time Purchased")


    tree_tv = ttk.Style()

    tree = ttk.Treeview(cart_frame, columns=columns, show="headings", height=33)
    tree.heading("#", text="#")
    tree.heading("Item name", text="Item name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Time Purchased", text="Time Purchased")
    tree.column("#", width=30, anchor=CENTER)
    tree.column("Item name", width=200)
    tree.column("Quantity", width=100, anchor=CENTER)
    tree.column("Price", width=100, anchor=CENTER)
    tree.column("Time Purchased", width=150, anchor=CENTER)
    tree.place(x=30,y=100, width=600)

    tree_tv.configure("Treeview", font=("Serif", 10))

    button_frames = ctk.CTkFrame(cart_frame, border_color="#333333", width=200, height=687, corner_radius=30, fg_color="#f2f2f2")
    button_frames.place(x=650,y=100)

    remove_order = ctk.CTkButton(button_frames, text="Remove order", fg_color="#379777", width=150, height=100, anchor=CENTER, font=("Serif", 15, "bold"), command=lambda:remove_order_one())
    remove_order.place(x=25, y=30)

    remove_all_order = ctk.CTkButton(button_frames, text="Remove all order", fg_color="#379777", width=150, height=100, anchor=CENTER, font=("Serif", 15, "bold"), command=lambda:remove_all())
    remove_all_order.place(x=25, y=150)

    hide_invoice = ctk.CTkButton(button_frames, text="Hide invoice", fg_color="#379777", width=150, height=100, anchor=CENTER, font=("Serif", 15, "bold"), command=lambda:hide_invoice())
    hide_invoice.place(x=25, y=270)

    confirm_order = ctk.CTkButton(button_frames, text="Confirm order", fg_color="#379777", width=150, height=100, anchor=CENTER, font=("Serif", 15, "bold"), command=lambda:confirm_order_func())
    confirm_order.place(x=25, y=390)

    is_on = True
    def hide_invoice():
        nonlocal is_on
        if is_on:
            invoice.place_forget()
            is_on = False
        else:
            invoice.place(x=880,y=100)
            is_on = True

    invoice = ctk.CTkTextbox(cart_frame, width=500, height=687, font=("Serif", 13), text_color="#000000", fg_color="#f2f2f2", state="disabled")
    invoice.place(x=880,y=100)


    order_counter = 1
    item_names = []
    item_prices = []
    item_quantity = []
    time_order_info = []

    def change_back_logged():
        # Open the file in read and write mode ('r+')
        try:
            with open('CREDS/user_creds.json', 'r+') as login_file:
                # Load JSON data from the file
                login_details = json.load(login_file)
                
                user_found = False
                
                # Iterate through each user credential
                for each_login in login_details["user_credentials"]:
                    if each_login.get("is_logged_in", False):
                        each_login["is_logged_in"] = False
                        user_found = True
                
                # Move the file pointer to the beginning and write back the updated JSON data
                login_file.seek(0)
                json.dump(login_details, login_file, indent=4)
                login_file.truncate()  # Truncate to remove any extra content
        except FileNotFoundError:
            return None

    def remove_all():
        
        if not tree.get_children():
            messagebox.showwarning("ALERT!", "You are deleting nothing...")
            return
        
        
        for child in tree.get_children():
            tree.delete(child)
            item_names.clear() 
            item_prices.clear() 
            time_order_info.clear()
            invoice_test()

    def create_shop_item(parent, image_path, item_name, item_price, row, column):
        item_frame = ctk.CTkFrame(parent, width=310, height=330, fg_color="#f2f2f2")
        item_frame.grid(row=row, column=column, padx=10, pady=10)

        item_image = image_loader(image_path)
        
        image_label = ctk.CTkLabel(item_frame, image=item_image, text=None)
        image_label.place(x=30, y=10)
        image_label.image = item_image  # Keep a reference to the image object

        name_label = ctk.CTkLabel(item_frame, text=item_name, font=("Serif", 25, "bold"), text_color="#000000")
        name_label.place(x=30, y=250)

        price_label = ctk.CTkLabel(item_frame, text=item_price, font=("Serif", 18), text_color="#000000")
        price_label.place(x=30, y=290)

        def add_to_cart():
            nonlocal order_counter
            
            name = name_label.cget('text')
            price = price_label.cget('text')
            
            if messagebox.askyesno("ALERT!", f"Do you want to add {name} to the cart?"):
                # Prompt user for quantity
                tite = ctk.CTkInputDialog(text="Please enter the quantity:", title="Test")
                quantity = tite.get_input()
                # Validate quantity input
                if quantity is None or quantity == []:
                    messagebox.showwarning("ALERT!", "Please enter a quantity")
                    return
                elif quantity == "":
                    quantity = 1
                
                # Calculate total price for this item
                total_price = int(price) * int(quantity)
                cur_TD = datetime.datetime.now()
                current_time = cur_TD.strftime("%Y-%m-%d %I:%M:%S %p")
                
                # Add item to the treeview
                tree.insert("", "end", values=(f"{order_counter}", name, quantity, total_price,current_time))
                
                # Update global order counter
                order_counter += 1
                
                # Update item names and prices lists
                item_names.append(name)
                item_prices.append(total_price)
                item_quantity.append(quantity)
                time_order_info.append(current_time)

                # Clear and update invoice display
                invoice.configure(state="normal")
                invoice_test()
            else:
                return None
                
        add_cart_btn = ctk.CTkButton(item_frame, text="Add to cart", font=("Serif", 20, "bold"), command=add_to_cart)
        add_cart_btn.place(x=150, y=290)

    def invoice_test():
        # Clear previous content in the Text widget
        invoice.configure(state="normal")
        invoice.delete("1.0", END)
        
        # Insert header and initial content
        invoice.insert('1.0', "========================SHOP-IT==============================\n")
        invoice.insert(END, "    #\t\tITEM NAME\t\tQUANTITY\t\tPRICE\n")
        
        # Iterate through items in the cart (treeview)
        index = 1
        for child in tree.get_children():
            item_values = tree.item(child, 'values')
            invoice.insert(END, f"    {item_values[0]}\t\t{item_values[1]}\t\t{item_values[2]}\t\t${item_values[3]}\n")
            index += 1
        
        # Insert total line
        invoice.insert(END, f"\n\t\t\t\t\t\t   Total: ${sum(item_prices):.2f}\n")
        
        # Disable editing in the invoice display
        invoice.configure(state="disabled")

    def remove_order_one():
        # Get selected item(s) from the treeview
        selected_items = tree.selection()
        remove_item = tree.item(selected_items)['values']
        
        if not selected_items:
            messagebox.showwarning("Warning", "Please select an item to delete.")
            return
        
        for item in selected_items:
            # Delete item from the treeview
            tree.delete(item)
            item_names.remove(remove_item[1]) # updates the items in the list
            item_prices.remove(remove_item[3]) # updates the invoice total
            time_order_info.remove(remove_item[4])
        # Update invoice display after deletion
        invoice_test()

    def confirm_order_func():
        
        if item_names == [] or item_prices == []:
            messagebox.showwarning("Alert!", "Your cart is empty...")
            return
        
        if messagebox.askyesno("ALERT!", "Ayou done shopping?"):
            
            for name, price, quantity,time in zip(item_names, item_prices, item_quantity,time_order_info):
                data = {
                    "Item name": name,
                    "Price": price,
                    "Quantity": quantity,
                    "Time purchased": time
                }                      
                # Check if file exists
                if os.path.exists("CREDS/sell_history.json"):
                    with open("CREDS/sell_history.json", 'r') as readF:
                        read = json.load(readF)
                    
                    # with open('CREDS/user_creds.json', 'r') as readF:
                    #     read1 = json.load(readF)
                        
                else:
                    read = {"Product_sold":[]}
                    # read1 = {"user_credentials":[]}
                # Append new data
                read["Product_sold"].append(data)
                
                # Write updated data back to file
                with open("CREDS/sell_history.json", 'w') as updF:
                    json.dump(read, updF, indent=4)
                    
            item_names.clear()# updates the items in the list
            item_prices.clear() # updates the invoice total
            time_order_info.clear()

            # Clear treeview
            for row in tree.get_children():
                tree.delete(row)
                
            with open('CREDS/user_creds.json', 'r+') as user_file:
                user_data = json.load(user_file)
                
            print(user_data)
            
            
            invoice_test()
            messagebox.showinfo("Thanks", "Thank you for shopping on Shop-IT")
        else:
            return None
        
    def confirm_order_func():
        if item_names == [] or item_prices == []:
            messagebox.showwarning("Alert!", "Your cart is empty...")
            return
        
        if messagebox.askyesno("ALERT!", "Are you done shopping?"):
            # Assume username_to_login is set somewhere in your application logic
            username_to_login =  user_name # Replace with actual username
            print(username_to_login)
            
            # Prepare order data
            order_data = []
            for name, price, quantity, time in zip(item_names, item_prices, item_quantity, time_order_info):
                data = {
                    "Item name": name,
                    "Price": price,
                    "Quantity": quantity,
                    "Time purchased": time
                }
                order_data.append(data)
            
            # Update user's orders history and total orders based on user type
            with open('CREDS/user_creds.json', 'r+') as login_file:
                login_details = json.load(login_file)
                
                for each_login in login_details["user_credentials"]:
                    if each_login["User_name"] == username_to_login:
                        if each_login["User_type"] == "Admin":
                            # Admin-specific actions (if needed)
                            pass
                        else:
                            # Regular user actions
                            each_login["Orders_History"].extend(order_data)
                            each_login["Total_Orders"] += len(order_data)
                        break  # Stop iterating once found
                
                # Write back the updated JSON data
                login_file.seek(0)
                json.dump(login_details, login_file, indent=4)
                login_file.truncate()
            
            # Clear cart items and update UI
            item_names.clear()
            item_prices.clear()
            time_order_info.clear()

            # Clear treeview (assuming 'tree' is your Treeview widget)
            for row in tree.get_children():
                tree.delete(row)
            
            # Update UI or perform additional actions
            invoice_test()
            messagebox.showinfo("Thanks", "Thank you for shopping on Shop-IT")
            change_accounts_details()
        else:
            return None 
            
        

    
    def exit_():
        if messagebox.askyesno("ALERT!", "Do you want to exit?"):
            change_back_logged()
            root.destroy()
            win.deiconify()
        else:
            return None

    # SHOPPING
    create_shop_item(scrollable_shop, "ITEMS\\bluetooth headphones.jpeg", "Headphones", "150", 0, 0)
    create_shop_item(scrollable_shop, "ITEMS\\bluetooth speaker.jpeg", "Bluetooth Speaker", "80", 0, 1)
    create_shop_item(scrollable_shop, "ITEMS\\cable.jpeg", "Charging Cable", "20", 0, 2)
    create_shop_item(scrollable_shop, "ITEMS\\external hard drive.jpeg", "External Hard Drive", "120", 0, 3)

    # 2nd row
    create_shop_item(scrollable_shop, "ITEMS\\camera.jpeg", "Camera", "500", 1, 0)
    create_shop_item(scrollable_shop, "ITEMS\\graphics card.jpg", "Graphics Card", "300", 1, 1)
    create_shop_item(scrollable_shop, "ITEMS\\laptop.jpg", "Laptop", "1000", 1, 2)
    create_shop_item(scrollable_shop, "ITEMS\\mouse.jpeg", "Mouse", "30", 1, 3)

    # 3rd row
    create_shop_item(scrollable_shop, "ITEMS\\keyboard.jpeg", "Keyboard", "70", 2, 0)
    create_shop_item(scrollable_shop, "ITEMS\\power supply.jpeg", "Power Supply", "90", 2, 1)
    create_shop_item(scrollable_shop, "ITEMS\\powerbank.jpeg", "Power Bank", "50", 2, 2)
    create_shop_item(scrollable_shop, "ITEMS\\ssd.jpg", "SSD", "150", 2, 3)

    # 4th row
    create_shop_item(scrollable_shop, "ITEMS\\motherboard.jpg", "Motherboard", "200", 3, 0)
    create_shop_item(scrollable_shop, "ITEMS\\printer.jpeg", "Printer", "120", 3, 1)
    create_shop_item(scrollable_shop, "ITEMS\\router.jpeg", "Router", "60", 3, 2)
    create_shop_item(scrollable_shop, "ITEMS\\switch.jpeg", "Switch", "40", 3, 3)

    # 5th row
    create_shop_item(scrollable_shop, "ITEMS\\ring light.jpeg", "Ring Light", "40", 4, 0)
    create_shop_item(scrollable_shop, "ITEMS\\usb drive.jpeg", "USB Drive", "25", 4, 1)
    create_shop_item(scrollable_shop, "ITEMS\\wall charger.jpeg", "Wall Charger", "15", 4, 2)
    create_shop_item(scrollable_shop, "ITEMS\\wireless mouse.jpeg", "Wireless Mouse", "50", 4, 3)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------ #
    change_accounts_details()
    root.protocol("WM_DELETE_WINDOW", exit_)
    root.mainloop()

# tite = ctk.CTk()
# main_shop(tite)
