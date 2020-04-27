from tkinter import *

root = Tk()
root.title("Slider Example App")
root.geometry("320x320")

vertical = Scale(root,from_=0,to=200)
vertical.pack()

horizontal = Scale(root,from_=0,to=100,orient=HORIZONTAL)
horizontal.pack()

def slide():
    label=Label(root,text=horizontal.get()).pack()

my_btn = Button(root,text="Click me!",command = slide).pack()

root.mainloop()
