from tkinter import *
import customtkinter
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox

current_theme = "dark"  # Default theme is light

def toggle_theme():
    global current_theme
    if current_theme == "light":
        current_theme = "dark"
    else:
        current_theme = "light"
    apply_theme()  # Apply the chosen theme

def apply_light_theme():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")
    listbox.configure(bg="white",fg="black",selectforeground="black")


def apply_dark_theme():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    listbox.configure(bg="#2D3033",fg="white")
def apply_theme():
    if current_theme == "light":
        apply_light_theme()
    else:
        apply_dark_theme()

def addtaskbutton():
    task = entry.get()  
    if task:  
        task = task.title()
        user_input.append(task)
        update_listbox()
        entry.delete(0, END)

def deletetaskbutton():
    selected_task = listbox.get(ACTIVE)  
    user_input.remove(selected_task)
    update_listbox()

def update_listbox():
    listbox.delete(0, END)  
    for task in user_input:
        listbox.insert(END, task)  


def reset_interface():
    confirm = messagebox.askyesno("Confirmation", "Do you wish to proceed?")
    if confirm:
        listbox.delete(0,END)
        user_input.clear()
        update_listbox()
   


def congratulations():
    messagebox.showinfo('Yayy!', 'Congratulations!! You have completed all tasks successfully!')
    reset_interface()
    update_listbox()
    
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root=customtkinter.CTk()
root.geometry("650x860")
root.title("To-Do List")

my_image = customtkinter.CTkImage(
                                  dark_image=Image.open("ToDoList.PNG"),
                                  size=(650, 220))
image_label = customtkinter.CTkLabel(master=root, image=my_image,width=200,height=100)
image_label.place(x=0, y=0)
#Main frame
frame = customtkinter.CTkFrame(master=root ,width=700, height=200)
frame.place(x=10,y=250)

listbox = Listbox(frame, width=30, height=10,bg="#2D3033", fg="white", selectbackground="#00A86B", selectforeground="white")
listbox.pack(padx=20, pady=10)
listbox_font = font.Font(family="Roboto",size=14)  
listbox.configure(font=listbox_font)

#Buttonframe
bframe=customtkinter.CTkFrame(master=root ,width=250, height=300)
bframe.place(x=400,y=246)

addbutton=customtkinter.CTkButton(master=bframe,width=200,height=35,text="Add Task")
addbutton.place(relx=0.5, rely=0.1,anchor=CENTER)
delbutton=customtkinter.CTkButton(master=bframe,width=200,height=35,text="Delete Task")
delbutton.place(relx=0.5, rely=0.25,anchor=CENTER)

#TypeTaskFrame
tframe=customtkinter.CTkFrame(master=root ,width=395, height=100)
tframe.place(x=200,y=570, anchor=CENTER)


entry = customtkinter.CTkEntry(master=tframe,width=350,height=80, placeholder_text="Type your task here....")
entry.pack(padx=20, pady=10)
theme_button = customtkinter.CTkButton(master=root, width=200, height=35, text="Toggle Theme",corner_radius=100)
theme_button.place(relx=0.81, rely=0.79, anchor=CENTER)
theme_button.configure(command=toggle_theme)

reset_button = customtkinter.CTkButton(master=bframe, width=200, height=35, text="Clear")
reset_button.place(relx=0.5, rely=0.40, anchor=CENTER)
reset_button.configure(command=reset_interface)

comp_button= customtkinter.CTkButton(master=bframe, width=200, height=35, text="Mark All Tasks as complete")
comp_button.place(relx=0.5, rely=0.55, anchor=CENTER)
comp_button.configure(command=congratulations)

addbutton.configure(command=addtaskbutton)
delbutton.configure(command=deletetaskbutton)

user_input=[]
apply_theme()
root.mainloop()


