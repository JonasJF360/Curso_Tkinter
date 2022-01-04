from tkinter import *

# ---------------------------------------------
# GUI
root = Tk()
root.title('App')

# ---------------------------------------------
# Widgets
frame_nome = Frame(root)
frame_endereco = Frame(root)

label_nome = Label(frame_nome, text='Nome:')
label_sobrenome = Label(frame_nome, text='Sobrenome:')
label_logradouro = Label(frame_endereco, text='Logradouro:')
label_cidade = Label(frame_endereco, text='Cidade:')

text_nome = Entry(frame_nome)
text_sobrenome = Entry(frame_nome)
text_logradouro = Entry(frame_endereco)
text_cidade = Entry(frame_endereco)

btn_salvar = Button(root, text='Salvar')

# ---------------------------------------------
# Layout
label_nome.grid(row=0, column=0, sticky=W)
label_sobrenome.grid(row=1, column=0, sticky=W)
text_nome.grid(row=0, column=1)
text_sobrenome.grid(row=1, column=1)

label_logradouro.grid(row=0, column=0, sticky=W)
label_cidade.grid(row=1, column=0, sticky=W)
text_logradouro.grid(row=0, column=1)
text_cidade.grid(row=1, column=1)

frame_nome.grid(row=0, column=0, padx=4, pady=2)
frame_endereco.grid(row=0, column=1, padx=4, pady=2)

btn_salvar.grid(column=0, columnspan=2)

root.mainloop()
