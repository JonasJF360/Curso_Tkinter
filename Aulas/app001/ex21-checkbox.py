from tkinter import *

def apresentar():
    msg.set('Valor: ' + str(vl_check.get()))

root = Tk()

vl_check = IntVar()  # 0 ou 1
msg = StringVar()

check = Checkbutton(
    root,
    text='Este é um checkbox',
    variable=vl_check,
    command=apresentar
).pack()

Label(root, textvariable=msg).pack()

root.mainloop()