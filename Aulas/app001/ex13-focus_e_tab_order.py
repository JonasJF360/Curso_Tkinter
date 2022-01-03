from tkinter import *

# Funções
def executar():
    l1['text'] = t1.get()
    l2['text'] = t2.get()
    l3['text'] = t3.get()

# GUI
root = Tk()
root.title('Login')

# widgets
t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

l1 = Label(root, text='')
l2 = Label(root, text='')
l3 = Label(root, text='')

b = Button(root, text='Executar', command=executar)

# layout
t1.grid()
t1.focus()  # Deixa o Entry t1 ativado ao iniciar
t2.grid()
t3.grid()

l1.grid()
l2.grid()
l3.grid()

b.grid()

root.mainloop()