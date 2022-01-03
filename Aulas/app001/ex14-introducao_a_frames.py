from tkinter import *

# Funções

# GUI
root = Tk()
root.title('Login')

# widgets
frame_login = Frame(root)

label_usuario = Label(frame_login, text='Usuário:')
label_senha = Label(frame_login, text='Senha:')
text_usuario = Entry(frame_login)
text_senha = Entry(frame_login)
cmd_entrar = Button(frame_login, text='Login')

# layout
label_usuario.grid(row=0, column=0, sticky=W)
label_senha.grid(row=1, column=0, sticky=W)
text_usuario.grid(row=0, column=1)
text_senha.grid(row=1, column=1)
cmd_entrar.grid(row=2, column=1, sticky=E)

frame_login.pack()

root.mainloop()