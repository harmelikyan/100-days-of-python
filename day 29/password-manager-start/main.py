from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_get = website_entry.get()
    email_get = email_username_entry.get()
    password_get = password_entry.get()
    new_data = {
        website_get: {
            "email": email_get,
            "password": password_get
        }
    }

    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_search = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found.")
    else:
        if website_search in data:
            email = data[website_search]["email"]
            password = data[website_search]["password"]
            messagebox.showinfo(message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(message=f"No details for {website_search} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Placeholder labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Placeholders
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(END, "harmelikyan@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", font=("Arial", 16), width=13, command=find_password)
search_button.grid(row=1, column=2)
gen_password_btn = Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(row=3, column=2)
add_button = Button(text="Add", font=("Arial", 16), width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
