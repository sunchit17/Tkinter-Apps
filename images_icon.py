from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Images and Icons example app")
root.iconbitmap("D:\Work\Tkinter_Apps\Icon.ico")

my_image = ImageTk.PhotoImage(Image.open("thor.jpg"))
my_label = Label(image=my_image, height=800, width=800)
my_label.pack()



root.mainloop()
