from functools import partial
from Tkinter import *
import Tkinter

root = Tkinter.Tk()
frame = Frame(root)
frame.pack()
MyButton = partial(Tkinter.Button,frame,fg="white",bg="blue")
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
qb = MyButton(text='Quit',bg="red",command=frame.quit)
b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X,expand=True)
root.title('PFAs!')
root.mainloop()