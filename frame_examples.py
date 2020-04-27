from tkinter import *

root=Tk()
root.title('Frame Examples')

frame = LabelFrame(root,text="This is a frame..",padx=25,pady=25)
frame.pack(padx=10,pady=10)

b=Button(frame,text="Don't CLick me!")
b2=Button(frame,text="Don't CLick me too!")
b.grid(row=0,column=0)
b2.grid(row=1,column=0)

root.mainloop()
