from tkinter import *

janela = Tk()
janela.title('Label Propriedades')
janela.geometry('500x500')

label1 = Label(janela)
label1['text'] = 'Frase label 02'
label1['font'] = 'Calibri 20'
label1['bd'] = 1
label1['relief'] = 'solid'
# label1.pack()

for item in label1.keys():
    print(item, ':', label1[item])

janela.mainloop()