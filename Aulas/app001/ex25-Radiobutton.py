from tkinter import *


def rfa1():
    print('Opção 01')


def ver_radio():
    msg['text'] = f'Opção {valor_a.get()} selecionada'


root = Tk()
root.config(padx=5, pady=5)

root.title('Radiobutton')
root.minsize(250, 200)
root.maxsize(300, 250)

frameA = Frame(root)
frameA.pack()
frameB = Frame(root)
frameB.pack()

valor_a = IntVar()
valor_b = IntVar()

rba1 = Radiobutton(frameA, text='Opção A 1', variable=valor_a,
                   value=1, command=rfa1, indicatoron=0)
rba1.pack()
rba2 = Radiobutton(frameA, text='Opção A 2', variable=valor_a, value=2)
rba2.pack()
rba3 = Radiobutton(frameA, text='Opção A 3', variable=valor_a, value=3)
rba3.pack()
rba3.select()

msg = Label(frameA, text='Nada selecionado')
msg.pack()

rbb1 = Radiobutton(frameB, text='Opção B 1', variable=valor_b, value=1)
rbb1.pack()
rbb2 = Radiobutton(frameB, text='Opção B 2', variable=valor_b, value=2)
rbb2.pack()
rbb3 = Radiobutton(frameB, text='Opção B 3', variable=valor_b, value=3)
rbb3.pack()
rbb2.select()

Button(root, text='Executar', command=ver_radio).pack()

root.mainloop()
