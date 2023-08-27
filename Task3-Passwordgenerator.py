from tkinter import *
import customtkinter
import random
import string

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root=customtkinter.CTk()
root.geometry("300x270")
root.title("Password Generator")
def generate_password():
    try:
        password_length = int(passentry.get())
        if password_length <= 0:
            genlabel.configure(text="Invalid length")
            return

        characters = ""
        if include_letters_var.get():
            characters += string.ascii_letters
        if include_digits_var.get():
            characters += string.digits
        if include_special_var.get():
            characters += string.punctuation
        
        if not characters:
            genlabel.configure(text="Select at least one character type")
            return

        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        genlabel.configure(text=generated_password)
    except ValueError:
        genlabel.configure(text="Invalid input")

include_letters_var = IntVar()
include_digits_var = IntVar()
include_special_var = IntVar()

#chooseframe=Frame(root,width=200,height=200,background="blue")
#chooseframe.place(x=50,y=180)
passlabel = customtkinter.CTkLabel(master=root,text="Password Length: ",font=("serif",13))
passlabel.place(x=10,y=10)
passentry = customtkinter.CTkEntry(master=root,width=100)
passentry.place(x=120,y=10)

include_letters_checkbox = customtkinter.CTkCheckBox(master=root, text="Include Letters", variable=include_letters_var,font=("serif",12))
include_letters_checkbox.place(x=10,y=50)

include_digits_checkbox = customtkinter.CTkCheckBox(master=root, text="Include Digits", variable=include_digits_var,font=("serif",12))
include_digits_checkbox.place(x=10,y=80)

include_special_checkbox = customtkinter.CTkCheckBox(master=root, text="Include Special Characters", variable=include_special_var,font=("serif",12))
include_special_checkbox.place(x=10,y=110)

genpass_button = customtkinter.CTkButton(master=root,text = "Generate Password",font=("serif",12),command=generate_password)
genpass_button.place(x=80,y=150)

genlabel = customtkinter.CTkLabel(master=root,text="",font=("serif",12),fg_color="#3b3b3b",width=200)
genlabel.place(x=50,y=200)

root.mainloop()