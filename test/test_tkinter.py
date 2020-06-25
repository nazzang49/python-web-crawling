from tkinter import *

def printHello():
    print('hello')

root = Tk()

w = Label(root, text='python-test')
b = Button(root, text='hello-python', command=printHello)

w.pack()
b.pack()

root.mainloop()