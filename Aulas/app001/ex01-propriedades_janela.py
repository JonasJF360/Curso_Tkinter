from tkinter import *  # Para pegar todas as propriedades do Tkinter | * = tudo/all

janela = Tk()  # Cria a janela.
janela.title('Primeiro app')  # Título

# Configuração para adicionar um icone no aplicativo.
try:  # Tentar esse comando
    janela.iconbitmap('images/icon.ico')
except:
    TclError  # Será executado se der esse erro
    icone = PhotoImage(file='images/icon.png')
    janela.iconphoto(False, icone)

# ('500x250') <- posição automática | Configura o tamanho e a posição da janela
janela.geometry('500x250+200+200')

# (TRUE, FALSE) ou (1, 0) | Controla o redimencionamento da janela.
janela.resizable(True, True)

# Configura o tamanho minimo ou o máximo da janela.
janela.minsize(width=500, height=250)
janela.maxsize(700, 400)

# Modo de inicialização da janela: "zoomed" = maximizada | "iconic" = minimizada | "normal" = padrão
# "withdrawn" =  não entendi esse | Obs.: "zoomed" só funciona no windows e Mac OS.
janela.state("normal")

janela.mainloop()  # Faz com que a janela apareça e aguarda uma ação.
