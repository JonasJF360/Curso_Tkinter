from tkinter import *

janela = Tk()
janela.title('Labels Tkinter')
# Tamanho e posicionamento da janela
largura = 300
altura = 150
posx = (janela.winfo_screenwidth() - largura) / 2
posy = (janela.winfo_screenheight() - altura) / 2 - 15
janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

# Contrução dos Lables e Button
label_1 = Label(janela, text='Este é o label 01.')
label_2 = Label(janela, text='Este é o label 02.')
cmd = Button(janela, text='Executar')

# Posição do pack()
cmd.pack()
label_2.pack()
label_1.pack()

janela.mainloop()