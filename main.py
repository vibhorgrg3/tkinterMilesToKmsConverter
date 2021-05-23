from tkinter import *


def changeTitle():
    cf = 1.609
    ans = cf * int(myEntry.get())
    myLabel3.config(text=ans)
    # myLabel1.pack()


# Window
window = Tk()
window.title("Miles to Kms")
window.minsize(width=200, height=100)
window.config(padx=10, pady=20)

# label 1

myLabel1 = Label(text='Miles')
# myLabel.pack()
myLabel1.config(padx=2,pady=2)
myLabel1.grid(column=2, row=0)

# label 2

myLabel2 = Label(text='is equal to')
myLabel2.config(padx=2,pady=2)
# myLabel.pack()
myLabel2.grid(column=0, row=1)

# label 3

myLabel3 = Label(text='0')
myLabel3.config(padx=2,pady=2)
# myLabel.pack()
myLabel3.grid(column=1, row=1)

# Button 1
myButton = Button(text='Calculate', command=changeTitle)
myButton.config(width=10,padx=2,pady=2)
myButton.grid(column=1, row=2)

# Input 1

myEntry = Entry()
# myEntry.config(width=10)
myEntry.grid(column=1, row=0)

window.mainloop()
