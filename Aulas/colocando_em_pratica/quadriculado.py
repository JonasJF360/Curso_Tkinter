from tkinter import *

root = Tk()
root.title('Quadriculado')

cor = 'black'
for linha in range(8):
    cor = 'black' if cor == 'white' else 'white'
    for coluna in range(8):
        cor = 'black' if cor == 'white' else 'white'
        Label(root, padx=15, pady=6, bg=cor).grid(row=linha, column= coluna)

root.mainloop()