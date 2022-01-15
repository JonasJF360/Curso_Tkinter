from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('Meu aplicativo')

        largura, altura = 600, 400
        posx = (self.winfo_screenwidth() - largura) / 2
        posy = (self.winfo_screenheight() - altura) / 2 - 25
        self.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
        self.resizable(0, 0)

        meuMenu = Menu(self)
        # Menu File
        fileMenu = Menu(meuMenu, tearoff=0)
        fileMenu.add_command(label='Novo')
        fileMenu.add_command(label='Abrir')
        fileMenu.add_command(label='Savar')
        fileMenu.add_separator()
        fileMenu.add_command(label='Configurações')
        fileMenu.add_command(label='Sair', command=self.exitApplication)
        meuMenu.add_cascade(label='Arquivos', menu=fileMenu)
        # Menu Edit
        editMenu = Menu(meuMenu, tearoff=0)
        editMenu.add_command(label='Copiar')
        editMenu.add_command(label='Colar')
        editMenu.add_command(label='Selecionar Tudo')
        meuMenu.add_cascade(label='Editar', menu=editMenu)

        self.config(menu=meuMenu)

    def exitApplication(self):
        msg = messagebox.askquestion(title='Sair', message='Deseja mesmo sair?')
        if msg == 'yes':
            self.destroy()


if __name__ == '__main__':
    root = App()
    root.mainloop()
