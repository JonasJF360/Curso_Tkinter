from tkinter import *

root = Tk()

# Icone do aplicativo
icone = PhotoImage(file='images/imagem1.png')
root.iconphoto(False, icone)

# Adicionando a imagem no app
# img = PhotoImage(file='images/imagem2.png')  # Imagem maior
img = PhotoImage(file='images/imagem1.png')  # Prefira por o tamanho desejado
add_imagem = Label(root, image=img).pack()

root.mainloop()
