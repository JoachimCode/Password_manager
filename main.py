# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter
from tkinter import messagebox
import random

window = tkinter.Tk()
window.title("Password")
window.config(padx=100, pady=20)
window.minsize(700,500)

def save():
    if len(website_name.get()) == 0 or len(password.get()) == 0 or len(email.get()) == 0:
        messagebox.showerror(title="Error", message="You left some entries empty")
        return None
    is_ok = messagebox.askokcancel(title=website_name.get(), message=f" Email: {email.get()} \nPassword: {password.get()}\n is it ok to save?")
    if is_ok == True:
        with open("data.txt", mode="a") as my_file:
            my_file.write(f"{website_name.get()} | {email.get()} | {password.get()} \n")
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

def generate_password():
    password_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    lists = [[random.choice(letters) for char in range(nr_letters)],[random.choice(numbers) for char in range(nr_numbers)],[random.choice(symbols) for char in range(nr_symbols)]]
    password_list = [i for sublist in lists for i in sublist]
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)



#Image
canvas = tkinter.Canvas()
canvas.config(height=200, width=200)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,100, image=image)
canvas.grid(column=1, row=0, padx=0)

#Website entry
website_name = tkinter.StringVar()
website_entry = tkinter.Entry()
website_entry.focus()
website_entry.config(width=50, textvariable=website_name)
website_entry.grid(column=1, columnspan=2, row=2)

#Website label
website_label = tkinter.Label()
website_label.config(text="Website:", font=24)
website_label.grid(column=0, row=2, ipadx=1)

#Email label
login = tkinter.Label()
login.config(text="Email/Username", font=24)
login.grid(column=0, row=3, padx=20)

#Email entry
email = tkinter.StringVar()
login_entry = tkinter.Entry()
login_entry.config(width=50, textvariable=email)
login_entry.insert(tkinter.END, "@gmail.com",)
login_entry.grid(column=1, row=3, columnspan=2)

#Password Label
password_label = tkinter.Label()
password_label.config(text="Password:", font=24)
password_label.grid(row=4, column=0)

#Password entry
password = tkinter.StringVar()
password_entry = tkinter.Entry()
password_entry.config(width=25, textvariable=password)
password_entry.grid(column=1, row=4, ipadx=0)

#Generate Password
generate = tkinter.Button()
generate.config(text="Generate Password", font=1, height=1, command=generate_password)
generate.grid(column=2, row=4, pady=5)

#ADD
add_button = tkinter.Button()
add_button.config(text="Add", width=40, command=save)
add_button.grid(column=1, columnspan=2, row=5)


window.mainloop()