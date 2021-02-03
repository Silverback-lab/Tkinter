from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look! I clicked a button!!")
	myLabel.pack()

mybutton = Button(root, text="Click Me!", command=myClick, fg="red", bg="white")
mybutton.pack()

root.mainloop()

