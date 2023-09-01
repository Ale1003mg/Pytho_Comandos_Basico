#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("Prueba de funcionamiento de python")
root.geometry('450x100')

menu= Menu(root)
new_item=Menu(menu)
new_item.add_command(label="New")
menu.add_cascade(label='File',menu=new_item)
new_item.add_separator()
new_item.add_command(label="Edit")
new_item.add_separator()
new_item.add_command(label="Cerrar",command=root.destroy)

label=Label(root,text="ID",font=("Arial Bold", 10)).grid(column=0,row=1)
label2=Label(root,text="Nombre",font=("Arial Bold", 10)).grid(column=1,row=1)
label3=Label(root,text="Apellidos",font=("Arial Bold", 10)).grid(column=2,row=1)
label4=Label(root,text="Cedula",font=("Arial Bold", 10)).grid(column=3,row=1)
label5=Label(root,text="Telefono",font=("Arial Bold", 10)).grid(column=4,row=1)

entry=  Entry(root,width=10).grid(column=0,row=2)
#combo=ttk.Combobox(root)
#combo['Values']=(1,2,3,4,"Text")
#combo.current(1)
#combo.grid(column=1,row=2)
entry2=Entry(root,width=10).grid(column=1,row=2)
entry3=Entry(root,width=10).grid(column=2,row=2)
entry4=Entry(root,width=10).grid(column=3,row=2)
entry5=Entry(root,width=10).grid(column=4,row=2)

def clicked():
    messagebox.showinfo('Mensage Hermegente', 'Prueba')
    #messagebox.showwarning('Message title', 'Message content')  #shows warning message
    #messagebox.showerror('Message title', 'Message content')    #shows error message


btn=Button(root,text="Cerrar",command=root.destroy, bg="blue",fg="white")
#btn=Button(root,text="Cerrar", bg="blue",fg="white", command=clicked)
btn.grid(column=2,row=4)
#frm=ttk.Frame(root,padding=10)
#frm.grid()
#ttk.Label(frm, text="Prueba").grid(column=0,row=0)
#ttk.Button(frm,text="quit",command=root.destroy).grid(column=0,row=2)
#label.pack

root.config(menu=menu)

root.mainloop()