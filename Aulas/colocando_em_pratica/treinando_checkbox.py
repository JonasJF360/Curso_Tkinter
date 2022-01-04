from tkinter import *

# Funções e lista de dados
paises = [
    'Afeganistão', 'Albania', 'Algeria', 'Andorra',
    'Angola', 'Australia', 'Bolivia', 'Brasil',
    'Canada', 'China', 'Clile', 'Congo', 'Mexico',
    'Islandia', 'Israel', 'Estados Unidos', 'Zimbabwe'
]


def deletar():
    texto = list(lista.curselection())
    para_recursividade = 0  # Parar a volta da recursividade
    for i, j in enumerate(texto):
        if para_recursividade == 1:
            break
        try:
            if j + 1 == texto[i + 1]:
                continue
            else:
                para_recursividade = 1
                lista.delete(texto[0], texto[i])
                deletar()
        except:
            IndexError
            lista.delete(texto[0], texto[-1])


# cores
fundo = '#2d3b58'
fonte = '#ffffff'
selec_listbox = '#798aac'
cor_linha1 = '#97aacf'
fundo_listbox = '#a8bfee'

# GUI
root = Tk()
root.config(bg=fundo)
root.title('Apagando da lista')
largura = 500
altura = 400
posx = (root.winfo_screenwidth() - largura) / 2
posy = (root.winfo_screenheight() - altura) / 2 - 15
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
root.minsize(largura, altura)
root.maxsize(largura, altura)

# Widgets
show = Label(root, text='Selecione um ou mais países',
             bg=fundo, fg=fonte, font=('Verdana', 14))
show.pack(pady=5)

lista = Listbox(root, selectmode='multiple', bg=fundo_listbox,
                highlightbackground='#42506b',
                selectbackground=selec_listbox)
lista.pack(padx=10, expand=YES, fill='both')

for i, item in enumerate(paises):
    num = i + 1
    num = '0' + str(num) if num < 10 else num
    lista.insert(END,f' {num} - {item}')
    lista.itemconfig(i, bg=cor_linha1)

Button(root, text='Apagar', font='Verdana 10 bold',
       activebackground='#42506b', highlightbackground='#42506b',
       bg=fundo, activeforeground=fonte, fg=fonte, command=deletar
       ).pack(pady=5)


root.mainloop()
