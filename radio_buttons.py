from tkinter import *

root =Tk()
root.title('Radio Buttons Example')

#r = IntVar()
#r.set("1")

TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text,mode in TOPPINGS:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    mylabel = Label(root,text=value)
    mylabel.pack()

button = Button(root,text="Choose Topping",command=lambda: clicked(pizza.get()))
button.pack()



#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: clicked(r.get())).pack()

root.mainloop()
