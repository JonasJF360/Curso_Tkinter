from tkinter import *

janela = Tk()
janela.title('Layout Grid')
# janela.geometry('500x500')

label1 = Label(janela, text='Texto 01', font='Calibri 20',fg='yellow', bg='red')
label2 = Label(janela, text='Texto 02', font='Calibri 20',fg='yellow', bg='green')
label3 = Label(janela, text='Texto 03', font='Calibri 20',fg='yellow', bg='blue')

btn1 = Button(janela, text='Executar 01')
btn2 = Button(janela, text='Executar 02')
btn3 = Button(janela, text='Executar 03')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

janela.mainloop()