from tkinter import *
from tkinter import messagebox

# https://pythonguides.com/category/python-tutorials/python-tkinter/

janela = Tk()
janela.title('Messagebox')
janela.geometry('300x200')
janela.config(bg='#5FB691')

def msg1():
    messagebox.showinfo('information', 'Hi! You got a prompt.')
    messagebox.showerror('error', 'Something went wrong!')
    messagebox.showwarning('warning', 'accept T&C')
    messagebox.askquestion('Ask Question', 'Do you want to continue?')
    messagebox.askokcancel('Ok Cancel', 'Are You sure?')
    messagebox.askyesno('Yes|No', 'Do you want to proceed?')
    messagebox.askretrycancel('retry', 'Failed! want to try again?')

Button(janela, text='Click Me', command=msg1).pack(pady=50)

janela.mainloop()