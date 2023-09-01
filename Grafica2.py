from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Pruebas especiales ")

menu= Menu(window)
new_item=Menu(menu)
new_item.add_command(label="New")
menu.add_cascade(label='File',menu=new_item)
new_item.add_separator()
new_item.add_command(label="Edit")
new_item.add_separator()
new_item.add_command(label="Cerrar",command=window.destroy)

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab3= ttk.Frame(tab_control)

tab_control.add(tab1, text='First')

tab_control.add(tab2, text='Second')

tab_control.add(tab3,text="Three")

lbl1 = Label(tab1, text= 'label1').grid(column=0, row=0)

lbl2 = Label(tab2, text= 'label2').grid(column=0, row=0)

lbl3=Label(tab3,text="Three").grid(column=0,row=0)
tab_control.pack(expand=1, fill='both')

window.geometry('450x200')
window.config(menu=menu)
window.mainloop()