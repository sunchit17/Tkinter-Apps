from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root=Tk()
root.title('Matplotlib with Tkinter')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000,25000,5000)
    plt.hist(house_prices,25)
    plt.show()


btn_show = Button(root,text="Show Graph",command=graph)
btn_show.pack()

root.mainloop()
