import tkinter as tk
from random import choice


colors = [
    '#ff0000',
    '#ff5100',
    '#ffa500',
    '#ffe23f',
    '#ffff00',
    '#00da98',
    '#009cda',
    '#0051ff',
    '#fdffe8',
    '#a8bfee',
    '#777777',
    '#35ff3f',
    '#a918fd',
    '#ff00dd',
    '#ad5a0d',
    '#107973',
]

cor = choice(colors)
botao = cor
fundo = ''


def bg_color():
    global fundo, botao
    novo = choice(colors)
    while novo == fundo or novo == botao:
        novo = choice(colors)
    fundo = novo
    root.config(bg=novo)


def btn_color(event=None):
    global fundo, botao
    novo = choice(colors)
    while novo == fundo or novo == botao:
        novo = choice(colors)
    botao = novo
    btn['bg'] = novo


def mudar_tudo(event=None):
    btn_color()
    bg_color()


root = tk.Tk()
root.geometry('250x200')

btn = tk.Button(root, text='Cores', command=bg_color, bg=cor)
btn.bind('<Return>', btn_color)  # Techa enter
btn.bind('<KP_Enter>', mudar_tudo)  # Enter do teclado numérico


btn.focus()
btn.pack(expand=True)

root.mainloop()
