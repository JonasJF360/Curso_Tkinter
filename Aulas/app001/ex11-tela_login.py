from tkinter import *

root = Tk()
root.title('Login')

Label(root, text='Usuário:').grid(row=0, sticky=W)
Label(root, text='Senha:').grid(row=1, sticky=W)

usuario = Entry(root).grid(row=0, column=1)
senha = Entry(root).grid(row=1, column=1)

cmd_login = Button(root, text='Login').grid(row=2, column=1, sticky=E)

root.mainloop()