# this programme is to make a special grid window with the help of graphical interface
# tkinter is the library to provide basic graphical interface
from tkinter import *

from graphicalinterface import python11


def view_command():
    # for only one time entry
    list1.delete(0, END)
    for row in python11.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in python11.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    python11.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())



window = Tk()
# make the four label first
l1 = Label(window, text="title")
l1.grid(row=0, column=0)
l2 = Label(window, text="author")
l2.grid(row=0, column=2)
l3 = Label(window, text="year")
l3.grid(row=1, column=0)
l4 = Label(window, text="isbn")
l4.grid(row=1, column=2)
title_text = StringVar()
# make the four entry block too
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)
# just make the list bar first then configure the scrollbar within it
list1 = Listbox(window)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
# for making scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())

# make buttons of your window
b1 = Button(window, text="view all", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(window, text="add entry", width=12, command=add_command)
b2.grid(row=3, column=3)
b3 = Button(window, text="delete entry", width=12)
b3.grid(row=4, column=3)
b4 = Button(window, text="search entry", width=12, command=search_command)
b4.grid(row=5, column=3)
b5 = Button(window, text="update entry", width=12)
b5.grid(row=6, column=3)
b6 = Button(window, text="close", width=12)
b6.grid(row=7, column=3)

window = mainloop()
