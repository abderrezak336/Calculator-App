from tkinter import *
import math




window = Tk()



window.title("Calculator")

window.config(height=500, width=300)


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


text = Text(height=3, width=13, font=("ariel", 30, "bold"))
text.place(x=0, y=0)


#---------------------------------------all functions of buttons---------------------
def left_pre():
    text.insert(END, "(")

def right_pre():
    text.insert(END, ")")

def point():
    text.insert(END, ".")

def sqrt():
    text.insert(END, "()**0.5")

def subtract():
    text.insert(END, "-")

def add():
    text.insert(END, "+")

def multiply():
    text.insert(END, "*")

def division():
    text.insert(END, "/")

def pi():
    text.insert(END, "3.14")


def clear():
    text.delete("1.0", END)

def remove():
    text.delete("end-2c")

def nine():
    text.insert(END, "9")

def eight():
    text.insert(END, "8")

def seven():
    text.insert(END, "7")

def six():
    text.insert(END, "6")

def five():
    text.insert(END, "5")

def four():
    text.insert(END, "4")

def three():
    text.insert(END, "3")

def two():
    text.insert(END, "2")

def one():
    text.insert(END, "1")

def result():
    user_input = text.get("1.0", END)
    result = eval(user_input)
    text.insert("end", f"\n={result}")











#---------------------------all buttons---------------------------


clear_button = Button(text="C", font=("normal", 20, "bold"), command=clear)
clear_button.place(x=0, y=170)

division_button = Button(text="%", font=("normal", 20, "bold"), command=division)
division_button.place(x=50, y=170)

multiply_button = Button(text="X", font=("normal", 20, "bold"), command=multiply)
multiply_button.place(x=105, y=170)

remove_button = Button(text="R", font=("normal", 20, "bold"), command=remove)
remove_button.place(x=155, y=170)

subtract_button = Button(text="_", font=("normal", 20, "bold"), command=subtract)
subtract_button.place(x=207, y=170)

add_button = Button(text="+", font=("normal", 20, "bold"), command=add)
add_button.place(x=255, y=170)

seven = Button(text="7", font=("normal", 23, "bold"), command=seven)
seven.place(x=0, y=227)

eight = Button(text="8", font=("normal", 23, "bold"), command=eight)
eight.place(x=50, y=227)

nine = Button(text="9", font=("normal", 23, "bold"), command=nine)
nine.place(x=103, y=227)

four = Button(text="4", font=("normal", 23, "bold"), command=four)
four.place(x=0, y=290)

five = Button(text="5", font=("normal", 23, "bold"), command=five)
five.place(x=50, y=290)

six = Button(text="6", font=("normal", 23, "bold"), command=six)
six.place(x=103, y=290)

one = Button(text="1", font=("normal", 23, "bold"), command=one)
one.place(x=0, y=353)

two = Button(text="2", font=("normal", 23, "bold"), command=two)
two.place(x=50, y=353)

three = Button(text="3", font=("normal", 23, "bold"), command=three)
three.place(x=103, y=353)

sqrt = Button(text="√", font=("normal", 23, "bold"), command=sqrt)
sqrt.place(y=227, x=155)

left_pre = Button(text="(", font=("normal", 23, "bold"), command=left_pre)
left_pre.place(y=227, x=206)

right_pre = Button(text=")", font=("normal", 23, "bold"), command=right_pre)
right_pre.place(x=254, y=227)

point_button = Button(text=".", font=("normal", 22, "bold"), width=2, command=point)
point_button.place(x=0, y=416)

equal_button = Button(text="=", font=("normal", 22, "bold"), command=result)
equal_button.place(x=50, y=416)

pi = Button(text="Pi", font=("normal", 22, "bold"), width=2, command=pi)
pi.place(x=103, y=416)
#---------------------------------------------------------------------


window.mainloop()