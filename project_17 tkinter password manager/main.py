from tkinter import *
from tkinter import messagebox
import json
import string
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END) # reset the entry field

    all_possible_chars = string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ""
    random_num = random.randint(12, 16)
    
    for i in range(random_num):
        password += random.choice(all_possible_chars)
    
    password_entry.insert(0, password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(): 
    website = website_entry.get()   
    username = email_username_entry.get()
    pw = password_entry.get()   

    if website == "" or pw == "":
        messagebox.showinfo(title="Error!", message="You forgot to add some information!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Website: {website}\n Username: {username}\n Password: {pw}\n Is it okay to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                to_be_added = f"{website} || {username} || {pw}\n"
                file.write(to_be_added)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            messagebox.showinfo(title="Success", message="The information was saved!")
        

    



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(""
"Password Manager")
window.geometry("600x500")
window.config(padx=20, pady=20)

# CANVAS
canvas = Canvas(width=200, height=200, highlightthickness=1)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website Entry
website_entry = Entry()
website_entry.grid(column=1, row=1)


# Email/Username Label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)


# Email/Username Entry
email_username_entry = Entry()
email_username_entry.grid(column=1, row=2)
email_username_entry.focus()
email_username_entry.insert(0, "emailliame@website.com")

# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password Entry
password_entry = Entry()
password_entry.grid(column=1, row=3)

# Password Button
password_button = Button(text="Generate Password", width=15, command=password_generator)
password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=18, command=save_password)
add_button.grid(column=1, row=4)

window.mainloop()
