from tkinter import *

janela = Tk()
janela.title('Propriedades Labels')
janela.geometry('500x500')

""" # Fonte, with e quebra de linha
label_1 = Label(janela,
                text='Este é meu label 01',
                font='Verdana 10',  # Fonte 10
                width=20,  # O width é proporcional ao tamanto da fonte.
                bg='#00ff00'
                ).pack()

label_2 = Label(janela,
                text='Este é meu label 02',
                font='Verdana 20',  # Fonte 20
                width=20,  # O width é proporcional ao tamanto da fonte.
                bg='#ff0000'
                ).pack()

label_3 = Label(
    janela,
    text='Frase 01\n\nFrase 02',
    font='Verdana 15',
    bd=1,  # ou borderwidth=1,
    relief='solid'
).pack() """

""" borda = 4
# Tipos de bordas
tiposbordas = Label(
    janela,
    text='solid',
    font='Verdana 10',
    bd=borda,  # ou borderwidth=1,
    relief='solid'
).pack()
tiposbordas = Label(
    janela,
    text='groove',
    font='Verdana 10',
    bd=borda,  # ou borderwidth=1,
    relief='groove'
).pack()
tiposbordas = Label(
    janela,
    text='flat',
    font='Verdana 10',
    bd=borda,  # ou borderwidth=1,
    relief='flat'
).pack()
tiposbordas = Label(
    janela,
    text='raised',
    font='Verdana 10',
    bd=borda,  # ou borderwidth=1,
    relief='raised'
).pack()
tiposbordas = Label(
    janela,
    text='sunken',
    font='Verdana 10',
    bd=borda,  # ou borderwidth=1,
    relief='sunken'
).pack()
tiposbordas = Label(
    janela,
    text='ridge',
    font='Verdana 10',
    bd=borda,  # ou borderwidth=1,
    relief='ridge'
).pack() """

# Altura e alinhamento
tiposbordas = Label(
    janela,
    text='0123456789\n0123456789\n0123456789\n0123456789\n0123456789',
    font='Ubuntu 15',
    bd=1,
    relief='solid',
    width=10,  # O width é proporcional ao tamanto da fonte.
    height=2   # O heighr é proporcional ao tamanto da fonte e referente quantidade de quebras de linha.
).pack()

"""
North ->  . N .
West  ->  W-|-E  <- Esst
South ->  ' S '
"""
tiposbordas = Label(
    janela,
    text='0123456789',
    font='Ubuntu 15',
    bd=1,
    relief='solid',
    width=25,  # O width é proporcional ao tamanto da fonte.
    height=4,  # O heighr é proporcional ao tamanto da fonte e referente quantidade de quebras de linha.
    anchor=NW  # ou "NW"(entre aspas) | Pose ser N, NE, E, SE, S, SW, W, NW ou CENTER(Esse é o padão)
).pack()

janela.mainloop()
