from tkinter import *

janela = Tk()
janela.title('Textvariable e Stringvar')
janela.geometry('500x500')

texto = StringVar()
texto.set('Olá, mundo!')

label1 = Label(
    janela,
    text=texto,  # Isso terá um problema
    font='Arial 20',
    bg='red',
    fg='white'
).pack()

label2 = Label(
    janela,
    textvariable=texto,
    font='Arial 20',
    bg='blue',
    fg='white'
).pack()
label3 = Label(
    janela,
    textvariable=texto,
    font='Arial 20',
    bg='blue',
    fg='white'
).pack()
label4 = Label(
    janela,
    textvariable=texto,
    font='Arial 20',
    bg='blue',
    fg='white'
).pack()

texto.set('Novo texto')

janela.mainloop()