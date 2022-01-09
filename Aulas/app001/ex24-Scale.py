from tkinter import *


def ver_valor(self):
    """ print(self) """
    valor_slide1.set(f'Valor: {slide1.get()}')

def pegar_valor():
    valor_slide2.set(f'Valor: {slide2.get()}')

root = Tk()
root.title('Scale')
root.geometry('300x200')
root.resizable(False, False)

slide1 = Scale(root,
              from_=0,
              to=100,
              orient='horizontal',
              resolution=4,
              command=ver_valor)
slide1.pack()

valor_slide1 = StringVar()
valor_slide1.set('Valor: 0')

Label(root, textvariable=valor_slide1).pack()

slide2 = Scale(root,
              from_=0,
              to=99.5,
              orient='horizontal',
              resolution=0.5
              )
slide2.pack()

valor_slide2 = StringVar()
valor_slide2.set('Valor: 0.0')

Label(root, textvariable=valor_slide2).pack()

btn = Button(root, text='Pegar valor', command=pegar_valor)
btn.pack()

root.mainloop()
