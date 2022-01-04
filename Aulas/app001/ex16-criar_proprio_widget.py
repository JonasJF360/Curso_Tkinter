from tkinter import *

# ---------------------------------------------
# O meu widget
class MeuFrame(Frame):  # sub-classe de uma super-classe
    def __init__(self, meuMaster):
        super().__init__()  # Inicia(obtem) todas as propriedades da super-classe(Frame)
        self['width'] = 500
        self['height'] =200
        self['bd'] = 2
        self['relief'] = SOLID
        self['padx'] = 5
        self['pady'] = 5

        Label(self, text='Nome:').grid(row=0, column=0, sticky=W)
        Entry(self).grid(row=0, column=1)


# ---------------------------------------------
# GUI
root = Tk()
root.title('App')

frame1 = MeuFrame(root).pack(padx=5, pady=5)
frame2 = MeuFrame(root).pack(padx=5, pady=5)
frame3 = MeuFrame(root).pack(padx=5, pady=5)
frame4 = MeuFrame(root).pack(padx=5, pady=5)

root.mainloop()
