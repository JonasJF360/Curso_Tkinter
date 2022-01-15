from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Login')
        largura, altura = 280, 130
        posx = (self.winfo_screenwidth() - largura) / 2
        posy = (self.winfo_screenheight() - altura) / 2 - 25
        self.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
        self.resizable(0, 0)

        # UI options
        paddings = {'padx': 20, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = StringVar()
        password = StringVar()

        # heading
        heading = ttk.Label(self, text='Tela de Login', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=N)

        # username
        username_label = ttk.Label(self, text="Usuário:")
        username_label.grid(column=0, row=1, sticky=W, **paddings)

        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=1, sticky=E, **paddings)

        # password
        password_label = ttk.Label(self, text="Senha:")
        password_label.grid(column=0, row=2, sticky=W, **paddings)

        password_entry = ttk.Entry(
            self, textvariable=password, show="*", **entry_font)
        password_entry.grid(column=1, row=2, sticky=E, **paddings)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))


if __name__ == "__main__":
    app = App()
    app.mainloop()
