from tkinter import *

# Fahrenheit para ceucius

# Funções
def converter():
    try:
        f = float(fahrenheit.get())
        c = (f-32) * 5/9
        resultado.set(str(round(c, 1)) + ' graus Ceucius')
    except:
        ValueError
        resultado.set('Algo está errado')


# GUI
root = Tk()
root.title('')
frame1 = Frame(root)
resultado = StringVar()

# widgets
label_titulo = Label(frame1, font='Verdana 9 bold', text='Valor em Fahrenheit')
fahrenheit = Entry(frame1)
cmd_entrar = Button(frame1, text='Converter', command=converter)
ceucius = Label(frame1, textvariable=resultado)

# layout
label_titulo.pack()
fahrenheit.pack()
ceucius.pack()
cmd_entrar.pack()

frame1.pack(padx=10, pady=10)

root.mainloop()
