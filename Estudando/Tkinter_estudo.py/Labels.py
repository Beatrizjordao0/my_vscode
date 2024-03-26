# Tkinter from Bro_code
'''
25/03/24
'''

from tkinter import *

wd = Tk()

#       labels

caixa = Label(wd,                  # caixa para texto dentro da janela window
              text='Hello, World',            # texto dentro da label
              font=('Arial',40,'bold'),         # fonte, tamanho e estilo
              fg='#4287f5',                  # cor do texto
              bg='#2c403f',               # cor da parte de tras do texto
              relief= RAISED,          # estilo da borda da caixa de texto 
              bd=20)           #tamanho da borda


# caixa.place(x=600,y=350)       # Não preciso do caixa.pack() quando uso o place
caixa.pack()         # compila e confirma a presença do texto na janela window




wd.mainloop()

