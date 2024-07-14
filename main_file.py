# main.py
from tkinter import *
from tkinter import ttk, font
from PIL import ImageTk, Image
from LIBS.main_window_new import register_window, main_window
from tkinter import messagebox
import json, os
from LIBS.tools import decrypt_pw
import customtkinter as ctk
from LIBS.shopping_window import main_shop

log_in_win = Tk()
log_in_win.title("Log in Page")
app_Width_1, app_Height_1 = 500,500
log_in_win.resizable(False,False)
log_in_win.config(bg="#F4F3F2")

screen_Width_1, screen_Height_1 = log_in_win.winfo_screenwidth(), log_in_win.winfo_screenheight()
x,y = (screen_Width_1 / 2) - (app_Width_1 / 2), (screen_Height_1 / 2) - (app_Height_1/ 2)
log_in_win.geometry(f"{app_Width_1}x{app_Height_1}+{int(x)}+{int(y)}")


label_font = font.Font(family="Serif", size=16, weight="normal")

Label(log_in_win, text="Login", font=("Serif", 32, "bold"), bg="#F4F3F2", fg="#333333").place(x=30, y=30)

Label(log_in_win, text="Username", font=label_font, bg="#F4F3F2", fg="#333333").place(x=30, y=150)

user_entry = ctk.CTkEntry(log_in_win, font=("Serif", 16,"bold"), width=445, height=40, placeholder_text="your username here",fg_color="#379777", border_color="#379777",text_color="#F4F3F2", placeholder_text_color="#F4F3F2")
user_entry.place(x=30, y=180)

Label(log_in_win, text="Password", font=label_font, bg="#F4F3F2", fg="#333333").place(x=30, y=250)

password_entry = ctk.CTkEntry(log_in_win, font=("Serif", 16,"bold"), width=445, height=40, show="•", placeholder_text="your password here",fg_color="#379777", border_color="#379777",text_color="#F4F3F2", placeholder_text_color="#F4F3F2")
password_entry.place(x=30, y=280)

forgot_password = ctk.CTkButton(log_in_win, text="Forgot password?",hover_color="#074173", command=lambda:forgor_PW())
forgot_password.place(x=30, y=325)

open_eye_img = Image.open("ASSETS\\eye_open.png")
close_eye_img = Image.open("ASSETS\\eye_close.png")

log_in_win.open_eye_img = ctk.CTkImage(light_image=open_eye_img, size=(25,25))
log_in_win.close_eye_img = ctk.CTkImage(light_image=close_eye_img, size=(25,25))

show_pw = ctk.CTkButton(log_in_win, text="show password",hover_color="#074173", image=log_in_win.close_eye_img, command=lambda:show_password(), font=("Serif", 12))
show_pw.place(x=335, y=325)

login_img = Image.open("ASSETS\\right_arrow.png")
log_in_win.login_img = ctk.CTkImage(light_image=login_img, size=(25,25))

log_in = ctk.CTkButton(log_in_win, text="Log in", font=("Serif", 16, "bold"), command=lambda:login(), width=445, height=40, image=log_in_win.login_img, compound=RIGHT, anchor=CENTER, hover_color="#074173")
log_in.place(x=30, y=400)

register_btn = ctk.CTkButton(log_in_win, text="Register", font=("Serif", 16, "bold"), command=lambda:register_window(log_in_win), width=445, height=40, image=log_in_win.login_img, compound=RIGHT, anchor=CENTER, hover_color="#074173")
register_btn.place(x=30, y=450)


is_on = True
def show_password():
    # a toggle button that shows and hide password
    global is_on
    if is_on:
        password_entry.configure(show="")
        show_pw.configure(image=log_in_win.open_eye_img)
        is_on = False
    else:
        password_entry.configure(show="•")
        show_pw.configure(image=log_in_win.close_eye_img)
        is_on = True

def forgor_PW():
    # fetches the password from the database incase of lost
    username = user_entry.get()
    
    if not username:
        messagebox.showinfo("Alert!", "Please type in username entry\nwhat you remember..")
        return
    
    with open("CREDS\\user_creds.json", 'r') as readF:
        data = json.load(readF)
    
    for each in data["user_credentials"]:
        if each["User_name"] == str(username):
            password = decrypt_pw(each['Password'])
            user_name = each["User_name"]
            messagebox.showinfo("Password!", f"Here is your password:\nUsername:{user_name}\nPassword:{password}")
            break
    else:
        messagebox.showerror("ERROR", "The username you type doesn't exist... Please register.")
        user_entry.delete(0, END)

def login():
    # validates the user determining if they are a Regular user or Admin
    username = user_entry.get()
    password = password_entry.get()

    # Fetch/retrieve data from the json file - credentials.json
    with open('CREDS/user_creds.json', 'r+') as login_file:
        login_details = json.load(login_file)
        user_found = False

        for each_login in login_details["user_credentials"]:
            if username == each_login["User_name"] and password == decrypt_pw(each_login["Password"]):
                if each_login["User_type"] == "Regular":
                    user_found = True
                    each_login["is_logged_in"] = True  # Mark the user as logged in
                else:
                    each_login["is_logged_in"] = None
                
                login_file.seek(0)
                json.dump(login_details, login_file, indent=4)
                login_file.truncate()

                user_entry.delete(0, END)
                password_entry.delete(0, END)

                if each_login["User_type"] == "Admin":
                    main_window(log_in_win)
                else:
                    main_shop(log_in_win)
                break

        if not user_found:
            try:
                user_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showerror("Alert!", "Wrong password or username...")
            except TclError:
                print("Error clearing entry fields. Login failed.")
 
def exit_():
    # ask the user if it wants to exit the app
    if messagebox.askyesno("ALERT!", "Do you want to exit?"):
        log_in_win.destroy()
    else:
        return None

log_in_win.protocol("WM_DELETE_WINDOW", exit_) # binds the exit_ when press the Close button "X"
log_in_win.mainloop()
