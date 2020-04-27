from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Box Example')

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my popup","Aur kaise hain aaplog")
    if response == 1:
        Label(root,text="Clicked yes").pack()
    else:
        Label(root,text="Clicked no").pack()    

Button(root,text="Popup",command=popup).pack()

root.mainloop()
