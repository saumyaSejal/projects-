from tkinter import *

def validate(option):
    value = option.get()
    print("through radio module",value)
    '''if value == "male":
        print("Welcome dude")
    elif value == "female":
        print("Welcome gurl")
    else:
        print("An option must be selected")'''

root = Tk()
root.geometry("400x400")

option = StringVar()
R1 = Radiobutton(root, text="MALE", value="male", var=option)
R2 = Radiobutton(root, text="FEMALE", value="female", var=option)
button = Button(root, text="OK", command=validate)

R1.pack()
R2.pack()
button.pack()

root.mainloop()