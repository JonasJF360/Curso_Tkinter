from tkinter import *

janela = Tk()
janela.title('Estilos de texto')
janela.geometry('500x300')

label_1 = Label(janela,
                text='Este é o label 01',
                bg='#ffff00',    # Cor fundo
                fg='#ff0000',    # Cor letra
                font='Ubuntu'    # Tipo de letra
)
label_2 = Label(janela,
                text='Este é o label 02',
                bg='#00ffff'  ,  # Cor fundo
                fg='#0000ff',    # Cor letra
                font='Times 25'  # Tipo e tamanho
)
label_3 = Label(janela,
                text='Este é o label 03',
                bg='#00ff00'  ,  # Cor fundo
                fg='#000000',    # Cor letra
                font='Verdana 15 bold italic'  # Tipo e tamanho
)

label_1.pack()
label_2.pack()
label_3.pack()

janela.mainloop()