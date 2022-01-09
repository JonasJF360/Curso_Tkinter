from tkinter import *
from tkinter import messagebox

def exitApplication():
    msg = messagebox.askquestion(title='Sair', message='Deseja mesmo sair')
    if msg == 'yes':
        root.destroy()

root = Tk()
root.title('Message')
root.geometry('300x200')
root.resizable(False, False)


meuMenu = Menu(root)

# Menu File
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label='Novo')
fileMenu.add_command(label='Abrir')
fileMenu.add_command(label='Savar')
fileMenu.add_separator()
fileMenu.add_command(label='Configurações')
fileMenu.add_command(label='Sair', command=exitApplication)
meuMenu.add_cascade(label='Arquivos', menu=fileMenu)
# Menu Edit
editMenu = Menu(meuMenu, tearoff=0)
editMenu.add_command(label='Copiar')
editMenu.add_command(label='Colar')
editMenu.add_command(label='Selecionar Tudo')
meuMenu.add_cascade(label='Editar', menu=editMenu)

root.config(menu=meuMenu)

root.mainloop()
