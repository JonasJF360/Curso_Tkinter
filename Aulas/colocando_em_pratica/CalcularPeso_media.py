from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Saber Médias')

        largura = 290
        altura = 200
        posix = (self.winfo_screenwidth() - largura) / 2
        posiy = (self.winfo_screenheight() - altura) / 2 - 25
        self.geometry('%dx%d+%d+%d' % (largura, altura, posix, posiy))
        self.resizable(0, 0)

        # Fames ---------------------------------------------------
        ttk.Frame(self, relief='flat', width=280).grid(pady=7)
        frame1 = ttk.Frame(self, relief='flat', width=280)
        frame2 = ttk.Frame(self, relief='flat', width=280)
        frame3 = ttk.Frame(self, relief='flat', width=280)

        # Widgets -------------------------------------------------
        # Frame 02
        frame1.grid(pady=5, padx=45)
        ttk.Label(frame1, text='Insira os pesos das provas e as\nnotas referentes separando-as\npor uma vírgula.\nEx.: Peso: 8, 5 | Nota: 7, 3', justify='center',
                  font='Ubuntu 10 bold').grid(row=0, columnspan=2)

        # Frame 03
        frame2.grid(pady=5, padx=45)
        self.label_quantidade = StringVar()
        self.label_quantidade.set('Pesos:')
        Label(frame2, textvariable=self.label_quantidade).grid(
            row=1, column=0,  sticky=W)
        self.pesos = ttk.Entry(frame2, width=18)
        self.pesos.grid(row=1, column=1, padx=3)
        self.pesos.focus()
        self.pesos.bind('<Return>', self.ir_notas)
        self.pesos.bind('<KP_Enter>', self.ir_notas)

        ttk.Label(frame2, text='Notas:').grid(
            row=2, column=0, sticky=W)
        self.notas = ttk.Entry(frame2, width=18)
        self.notas.grid(row=2, column=1, padx=3)
        self.notas.bind('<Return>', self.calcular)
        self.notas.bind('<KP_Enter>', self.calcular)

        frame3.grid(pady=5, padx=45)
        self.media = StringVar()
        self.media.set('Média final: 0,00')
        Label(frame3, textvariable=self.media,
              font='Ubuntu 13 bold').grid(row=4, columnspan=2)

    def ir_notas(self, event=None):
        self.notas.focus()
        
    def calcular(self, event=None):
        vl_pesos = self.pesos.get()
        vl_pesos = vl_pesos.split(',')
        vl_notas = self.notas.get()
        vl_notas = vl_notas.split(',')
        if len(vl_pesos) != len(vl_notas):
            self.media.set('Erro nos valores!')
        else:
            try:
                pesoXnota = 0
                somaPeso = 0
                for i, j in enumerate(vl_pesos):
                    pesoXnota += float(vl_pesos[i]) * float(vl_notas[i])
                    somaPeso += float(j)
                if pesoXnota == 0 or somaPeso == 0:
                    self.media.set('Média final: Erro!')
                else:
                    self.media.set(f'Média final: {(pesoXnota / somaPeso):.2f}')

            except:
                self.media.set('Algo está errado!')


if __name__ == '__main__':
    app = App()
    app.mainloop()
