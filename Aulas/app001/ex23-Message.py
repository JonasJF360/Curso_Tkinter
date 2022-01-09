from tkinter import *

root = Tk()
root.title('Message')
#root.geometry('500x300')
root.resizable(False, False)

txt = Message(root,
              text='Essa é uma menságem usando o widget Messege!:\nMussum Ipsum, cacilds vidis litro abertis. Aenean aliquam molestie leo, vitae iaculis nisl mauris nec dolor in eros commodo tempor. Atirei o pau no gatis, per gatis num morreus si num tem leite então bota uma pinga aí cumpadi! mais vale um bebadis conhecidiss, que um alcoolatra anonimis nec orci ornare consequat. Praesent lacinia ultrices consectetur. Sed non ipsum felis quem num gosta di mé, boa gentis num é detraxit consequat et quo num tendi nada pra lá, depois divoltis porris, paradis mé faiz elementum girarzis, nisi eros vermeio.'
              )  # Obs.: 'width' não é relevante em textos curtos.
txt.pack(padx=5, pady=5)

root.mainloop()
