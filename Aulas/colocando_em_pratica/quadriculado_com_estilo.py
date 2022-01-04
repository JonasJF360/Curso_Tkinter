from tkinter import *

root = Tk()
root.title('Quadriculado')
root.geometry('350x340')
root.minsize(350, 340)
root.maxsize(350, 340)
root.config(bg='#424242')
root.config(padx=5)
root.config(pady=5)

cor = [
    '#ff0000',
    '#ff5100',
    '#ffa500',
    '#ffe23f',
    '#ffff00',
    '#00da98',
    '#009cda',
    '#0051ff'
]

for linha in range(8):
    f = Frame(root, bg='#424242')
    for coluna, vcor in enumerate(cor):
        Label(f, padx=15, pady=6, bg=vcor).pack(padx=5, side=LEFT)
    f.pack(pady=5, side=TOP)

root.mainloop()
