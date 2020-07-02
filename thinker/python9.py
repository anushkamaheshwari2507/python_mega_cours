# thinker is usually a module so first import everything from thinker
from tkinter import *

# first make a empty window

window = Tk()


# make a function to declare what to be print after pressing the button execute
def anu():
    print(abhi.get())
    t1.insert(END, abhi.get())


# first make a button on the window
b1 = Button(window, text="execute", command=anu)
# now you have to define where you want to place your button on the window
# b1.pack()
# but you must use grid method because you can have larger control on the row and columns of a grid of window
b1.grid(row=0, column=0)
# you can also rowspan as one more attribute of grid ...if you want your button to be extent upto 2 or many columns
# if you want to give entry in your window you can ues entry method do this with your entry block if you want that
# whatever the user gives in the text block will print after pressing the button
abhi = StringVar()
e1 = Entry(window, textvariable=abhi)
e1.grid(row=0, column=1)
# you can also make a text block in your window basically
# you are going to get a text block of full size along with ur window
# so you must give height and width along with text function because that is important to mention the size of the block
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
