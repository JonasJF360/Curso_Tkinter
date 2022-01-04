from tkinter import *

def comando():
    print(lista.index())
    #    lista.delete(0, END)

root = Tk()
# Criação do espaço para os itens
lista = Listbox(root, selectmode=EXTENDED)
lista.pack()

# Inserindo itens de um a um
""" lista.insert(END, 'Primeiro item da lista;')
lista.insert(END, 'Segungo item da lista;')
lista.insert(END, 'Terceiro item da lista;')
lista.insert(END, 'Quarto item da lista;') """

# Adicionasndo itens a partir de uma base de dados
# Obs.: Não precisa nescessáriamente ser uma lista.
elementos = [
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista',
    'item da lista'
]

for y, i in enumerate(elementos):
    x = '.' if y + 1 == len(elementos) else ';'
    lista.insert(END,f'Lista {y + 1} {i}{x}')

btn = Button(root, text='Excluir', command=comando)
btn.pack()

root.mainloop()
