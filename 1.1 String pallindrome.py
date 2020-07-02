'''
s = input("Enter string = ")
print('Original string = ',s)
print('Reverse string = ', s[::-1])
a = s[::-1]

if (s == a):
        print('haan')
else:
        print('No')
'''
from tkinter import *
from PIL import *

class Login_System:
        def __init__(self,root):
                # print('Hello')
                self.root = root
                self.root.title('Login System')
                self.root.geometry("1350x750+0+0")

                #Images
                self.bg_icon = Tk.PhotoImage(file = "images/Image.jpg")
                self.user_icon = PhotoImage(file = "images/Image.jpg")
                self.pass_icon = PhotoImage(file="images/Image.jpg")

                title = Label(self,root, text="Login System", font=("times new roman",40,"bold"))
                title.place(x=0,y=0,relwidth=1)


root = Tk()
obj = Login_System(root)
root.mainloop()