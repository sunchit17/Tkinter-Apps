from tkinter import *
root = Tk()

root.title("Calculator App")
e = Entry(root, width=50, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def btn_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_add():
    first_num = e.get()
    global f_num
    global f_math
    f_num=int(first_num)
    f_math="+"
    e.delete(0,END)

def button_subtract():
    first_num = e.get()
    global f_num
    global f_math
    f_num=int(first_num)
    f_math="-"
    e.delete(0,END)

def button_multiply():
    first_num = e.get()
    global f_num
    global f_math
    f_num=int(first_num)
    f_math="*"
    e.delete(0,END)

def button_divide():
    first_num = e.get()
    global f_num
    global f_math
    f_num=int(first_num)
    f_math="/"
    e.delete(0,END)

def button_equal():
    second_num=e.get()
    e.delete(0,END)
    if f_math == "+":
        e.insert(0,f_num+int(second_num))
    if f_math == "-":
        e.insert(0,f_num-int(second_num))
    if f_math == "*":
        e.insert(0,f_num*int(second_num))
    if f_math == "/":
        if int(second_num)==0:
            e.insert(0,"Divide by zero error")
        else:
            e.insert(0,f_num/int(second_num))


def button_clear():
    e.delete(0,END)

btn_1 = Button(root,text="1",padx=40,pady=20,command=lambda: btn_click(1))
btn_2 = Button(root,text="2",padx=40,pady=20,command=lambda: btn_click(2))
btn_3 = Button(root,text="3",padx=40,pady=20,command=lambda: btn_click(3))
btn_4 = Button(root,text="4",padx=40,pady=20,command=lambda: btn_click(4))
btn_5 = Button(root,text="5",padx=40,pady=20,command=lambda: btn_click(5))
btn_6 = Button(root,text="6",padx=40,pady=20,command=lambda: btn_click(6))
btn_7 = Button(root,text="7",padx=40,pady=20,command=lambda: btn_click(7))
btn_8 = Button(root,text="8",padx=40,pady=20,command=lambda: btn_click(8))
btn_9 = Button(root,text="9",padx=40,pady=20,command=lambda: btn_click(9))
btn_0 = Button(root,text="0",padx=40,pady=20,command=lambda: btn_click(0))
btn_add = Button(root,text="+",padx=39,pady=20,command=button_add)
btn_subtract = Button(root,text="-",padx=39,pady=20,command=button_subtract)
btn_multiply = Button(root,text="*",padx=41,pady=20,command=button_multiply)
btn_divide = Button(root,text="/",padx=41,pady=20,command=button_divide)
btn_equal = Button(root,text="=",padx=95,pady=20,command=button_equal)
btn_clear = Button(root,text="CLS",padx=89,pady=20,command=button_clear)


btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)

btn_0.grid(row=4,column=0)
btn_add.grid(row=5,column=0)
btn_equal.grid(row=5,column=1,columnspan=2)
btn_clear.grid(row=4,column=1,columnspan=2)

btn_subtract.grid(row=6,column=0)
btn_multiply.grid(row=6,column=1)
btn_divide.grid(row=6,column=2)

root.mainloop()
