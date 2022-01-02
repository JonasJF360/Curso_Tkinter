from tkinter import *

janela = Tk()
janela.title('Janela Centralizada')

# Dimenções da Janela
largura = 500
altura = 300

# Achar a dimenção da tela(display) do computador
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calculo da posição da janela
posx = (largura_tela - largura) / 2
posy = (altura_tela - altura) / 2 - 15  # -15 é opcional

# Geometry | janela.geometry(f'{largura}x{altura}+{int(posx)}+{int(posy)}') <-- também funciona
janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

janela.mainloop()