# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=100, pady=20)
window.minsize(700,500)

#Image
canvas = tkinter.Canvas()
canvas.config(height=200, width=200)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,100, image=image)
canvas.grid(column=1, row=0, padx=0)

#Website entry
website_entry = tkinter.Entry()
website_entry.config(width=50)
website_entry.grid(column=1, columnspan=2, row=2)

#Website label
website_label = tkinter.Label()
website_label.config(text="Website:", font=24)
website_label.grid(column=0, row=2, ipadx=1)

#Email label
login = tkinter.Label()
login.config(text="Email/Username:", font=24)
login.grid(column=0, row=3, padx=20)

#Email entry
login_entry = tkinter.Entry()
login_entry.config(width=50)
login_entry.grid(column=1, row=3, columnspan=2)

#Password Label
password_label = tkinter.Label()
password_label.config(text="Password:", font=24)
password_label.grid(row=4, column=0)

#Password entry
login_entry = tkinter.Entry()
login_entry.config(width=25)
login_entry.grid(column=1, row=4, ipadx=0)

#Generate Password
generate = tkinter.Button()
generate.config(text="Generate Password", font=1, height=1)
generate.grid(column=2, row=4, pady=5)

#ADD
add_button = tkinter.Button()
add_button.config(text="Add", width=40)
add_button.grid(column=1, columnspan=2, row=5)

window.mainloop()