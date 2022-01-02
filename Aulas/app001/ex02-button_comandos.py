from tkinter import *

janela = Tk()
# janela['bg'] = 'blue'  # Muda a cor de fundo
janela.title('Titulo')
janela.geometry('500x300')

def cmd_click(nome='José'):
    print(f'Olá, {nome}.')

def calculo(conteudo):
    print(eval(conteudo))

# Criando um botão simples
cmd = Button(janela, text='Executar 1', command=cmd_click)
cmd.pack()

cmd2 = Button(janela, text='Executar 2', command=lambda: cmd_click('Carlos'))
cmd2.pack()

cmd3 = Button(janela, text='Executar 3', command=lambda: calculo('9 * (3 + 5)')).pack()

janela.mainloop()


# Comando no terminal para listar as possibilidades de recursos
# que o Tkinter oferece para uso 
# python3
# >>> from tkinter import *
# >>> dir(Tk)
# ['_Misc__winfo_getint', '_Misc__winfo_parseitem',
#     ... ,
#     'wm_withdraw']
# >>> 