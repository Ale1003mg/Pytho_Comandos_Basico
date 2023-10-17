from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title("Calculadora")
root.geometry('450x200')


lbl=Label(root,text= "Calculadora")
lbl.anchor(CENTER)
lbl.grid(column=60,row=1)

num=Entry(root,width=30)
num.grid(column=60,row=3)
num2=Entry(root,width=30)
num2.grid(column=60,row=5)
btn= Button(root,text="+")
btn.grid(column=4,row=6)
btn2= Button(root,text="-")
btn2.grid(column=5,row=6)
btn3= Button(root,text="*")
btn3.grid(column=6,row=6)
btn3= Button(root,text="/")
btn3.grid(column=7,row=6)

root.mainloop()