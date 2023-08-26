from tkinter import *
import customtkinter
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry("400x525")
root.title("Calculator")


def clickbut(number):
    x = anslabel.configure(text=anslabel.cget("text") + number)

def operbut(operator):
    y = anslabel.configure(text= anslabel.cget("text") + operator)

def calculate():
    try:
        expression = anslabel.cget("text")
        
        # Replace π with its numerical value from the math module
        expression = expression.replace("π", str(math.pi))
        
        result = str(eval(expression))
        anslabel.configure(text=result)
    except Exception as e:
        anslabel.configure(text="Error")

def clear_label():
    anslabel.configure(text="")
def percent_button_click():
    current_text = anslabel.cget("text")
    
    try:
        value = float(current_text)
        result = value / 100
        anslabel.configure(text=str(result))
    except ValueError:
        anslabel.configure(text=current_text + "%")

def pi_button_click():
    anslabel.configure(text=anslabel.cget("text") + "π")
def decimal_button_click():
    anslabel.configure(text=anslabel.cget("text") + ".")

    
anslabel=customtkinter.CTkLabel(master=root,width=380,height=100,fg_color="#696969",text="",font=("serif", 40),text_color="white")
anslabel.place(x=10,y=10)

buttonframe=customtkinter.CTkFrame(master=root,width=380,height=390,fg_color="#1b1b1b")
buttonframe.place(x=10,y=120)

div_button=customtkinter.CTkButton(master=buttonframe,width=60,height=60,text="÷",fg_color="#ff8f00",corner_radius=70,hover_color=("white"),font=("serif",30))
div_button.place(x=300,y=10)

mul_button=customtkinter.CTkButton(master=buttonframe,width=60,height=60,text="×",fg_color="#ff8f00",corner_radius=70,hover_color=("white"),font=("serif",30))
mul_button.place(x=300,y=85)

min_button=customtkinter.CTkButton(master=buttonframe,width=60,height=60,text="−",fg_color="#ff8f00",corner_radius=70,hover_color=("white"),font=("serif",30))
min_button.place(x=300,y=160)

add_button=customtkinter.CTkButton(master=buttonframe,width=60,height=60,text="+",fg_color="#ff8f00",corner_radius=70,hover_color=("white"),font=("serif",30))
add_button.place(x=300,y=235)

equ_button=customtkinter.CTkButton(master=buttonframe,width=60,height=60,text="=",fg_color="#ff8f00",corner_radius=70,hover_color=("white"),font=("serif",30))
equ_button.place(x=300,y=310)

AC_button=customtkinter.CTkButton(master=buttonframe,width=50,height=60,text="AC",fg_color="#696969",corner_radius=70,hover_color=("#a9a9a9"),font=("serif",20),text_color="black")
AC_button.place(x=5,y=10)

per_button=customtkinter.CTkButton(master=buttonframe,width=60,height=60,text="%",fg_color="#696969",corner_radius=70,hover_color=("#a9a9a9"),font=("serif",20),text_color="black")
per_button.place(x=105,y=10)

pi_button=customtkinter.CTkButton(master=buttonframe,width=60,height=60,text="π",fg_color="#696969",corner_radius=70,hover_color=("#a9a9a9"),font=("serif",20),text_color="black")
pi_button.place(x=200,y=10)

sev_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="7",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
sev_button.place(x=10,y=80)

four_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="4",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
four_button.place(x=10,y=160)

one_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="1",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
one_button.place(x=10,y=240)

eight_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="8",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
eight_button.place(x=105,y=80)

five_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="5",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
five_button.place(x=105,y=160)

two_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="2",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
two_button.place(x=105,y=240)

nine_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="9",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
nine_button.place(x=200,y=80)

six_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="6",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
six_button.place(x=200,y=160)

three_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text="3",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
three_button.place(x=200,y=240)

zero_button=customtkinter.CTkButton(master=buttonframe,width=175,height=60,text="0",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",23))
zero_button.place(x=10,y=315)

point_button=customtkinter.CTkButton(master=buttonframe,width=65,height=60,text=".",fg_color="#3b3b3b",corner_radius=70,hover_color="#555555",font=("serif",25))
point_button.place(x=202,y=315)

number_buttons = [zero_button, one_button, two_button, three_button, four_button,
                  five_button, six_button, sev_button, eight_button, nine_button,
                  point_button]

operator_buttons = [add_button, min_button, mul_button, div_button]
operators = ["+", "-", "*", "/"]

for button, operator in zip(operator_buttons, operators):
    button.bind("<Button-1>", lambda event, op=operator: operbut(op))

for button, value in zip(number_buttons, "0123456789."):
    button.bind("<Button-1>", lambda event, val=value: clickbut(val))

equ_button.bind("<Button-1>", lambda event: calculate())
AC_button.bind("<Button-1>", lambda event: clear_label())

per_button.bind("<Button-1>", lambda event: percent_button_click())
pi_button.bind("<Button-1>", lambda event: pi_button_click())
point_button.bind("<Button-1>", lambda event: decimal_button_click())


root.mainloop()