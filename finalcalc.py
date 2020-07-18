from tkinter import *
import math
from mpmath import *
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import ttk

root = Tk()
root.title("Artistic Paradise Calc")
root.configure(bg="white")
root.geometry("552x365")
root.iconbitmap("D:/programming/Capture.PNG")
lab1 = Label(root, text="Calculator by Kavin Jindal", fg="black", bg="white", borderwidth=5 )
e=Entry(root, width=35, borderwidth=5, bg="white",fg="black",)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10, )
#e.insert(0, "Enter your Name: ")
font1=font.Font(size=15)



def button_click(number):
   #e.delete(100, END)
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)
    
    

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
       e.insert(0, f_num + int(second_number))
       
    if math == "subtraction":
       e.insert(0, f_num - int(second_number))
       
    if math == "multiplication":
       e.insert(0, f_num * int(second_number))
       
    if math == "division":
       e.insert(0, f_num / int(second_number))

    if math == "square":
       e.insert(0, f_num * f_num)

    if math == "cube":
       e.insert(0, f_num * f_num * f_num)

    if math == "square_root":
       e.insert(0, f_num**(1/2))

    if math == "cube_root":
       e.insert(0, f_num**(1/3))






          

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_square():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = int(first_number)
    e.delete(0, END)

def button_cube():
    first_number = e.get()
    global f_num
    global math
    math = "cube"
    f_num = int(first_number)
    e.delete(0, END)

def button_square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    e.delete(0, END)
    if math =="root":
       e.insert(0, math.sqrt(f_num))

def button_cube_root():
	first_number = e.get()
	global f_num
	global math
	math = "cube_root"
	f_num = float(first_number)
	e.delete(0, END)
	if math =="cube_root":
		e.insert(0, f_num**(1/3))

    

button_1 = Button(root, text="1", padx=40, pady=20,bg="white",fg="black",  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,bg="white",fg="black", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,bg="white",fg="black", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,bg="white",fg="black", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,bg="white",fg="black", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,bg="white",fg="black", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,bg="white",fg="black", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,bg="white",fg="black", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=21,bg="white",fg="black", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=152, pady=21,bg="white",fg="black", command=lambda: button_click(0))

#Functions

button_add = Button(root, text="+", padx=40, pady=20,bg="white",fg="black", command=button_add)
button_equal = Button(root, text="=", padx=152, pady=20,bg="white",fg="black", command=button_equal)
button_clear = Button(root, text="Clear", padx=82,  pady=20,bg="white",fg="black", command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20,bg="white",fg="black", command=button_subtract)
button_multiply = Button(root, text="x", padx=41, pady=20,bg="white",fg="black", command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20,bg="white",fg="black", command=button_divide)
button_square = Button(root, text="²", padx=41, pady=20,bg="white",fg="black", command=button_square)
button_cube = Button(root, text="³", padx=41, pady=20,bg="white",fg="black", command=button_cube)
button_square_root = Button(root, text="√", padx=41, pady=20,bg="white",fg="black", command=button_square_root)
button_cube_root = Button(root, text="∛x", padx=41, pady=20, bg="white", fg="black", command=button_cube_root)


button_quit = Button(root, text="Exit Program", padx=41, pady=20, bg="white", fg="black", command=root.quit)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0, columnspan=3)
button_clear.grid(row=5, column=3, columnspan=3)
button_equal.grid(row=5, column=0, columnspan=3)
button_add.grid(row=1, column=3)

button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_square.grid(row=1, column=4)
button_cube.grid(row=2, column=4)
button_square_root.grid(row=3, column=4)
button_cube_root.grid(row=4, column=4)



#fonts 


button_1['font'] = font1
button_2['font'] = font1
button_3['font'] = font1
button_4['font'] = font1
button_5['font'] = font1
button_6['font'] = font1
button_7['font'] = font1
button_8['font'] = font1
button_9['font'] = font1
button_0['font'] = font1
button_clear['font'] = font1
button_equal['font'] = font1
button_add['font'] = font1
button_subtract['font'] = font1
button_multiply['font'] = font1
button_divide['font'] = font1
button_square['font'] = font1
button_square_root['font'] = font1
button_cube['font'] = font1
button_cube_root['font'] = font1
e['font'] = font1







root.mainloop()
