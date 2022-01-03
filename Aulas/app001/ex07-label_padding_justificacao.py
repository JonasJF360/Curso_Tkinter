from tkinter import *

janela = Tk()
janela.title('Label Padding')
janela.geometry('500x500')

label_1 = Label(
    janela,
    text='Frase de teste',
    font='Arial 20',
    bd=1,
    relief='solid',
    padx=50,
    pady=50
).pack()

label_2 = Label(
    janela,
    text='Frase de teste\nFrase de teste 02\nTeste',
    font='Arial 20',
    bd=1,
    relief=SOLID,
    padx='10',
    pady=10,
    justify=LEFT  # ['left', 'center', 'right']
    
).pack()

label_3 = Label(
    janela,
    text='Frase de teste\nTeste',
    font='Arial 20',
    bd=1,
    relief=SOLID,
    width=20,
    height=4,
    justify='right',  # ['left', 'center', 'right']
    anchor=W
).pack()

janela.mainloop()