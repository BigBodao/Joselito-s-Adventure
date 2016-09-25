from tkinter import *
'''import tkinter as tk
from PIL import ImageTk, Image'''

class Janela:
    def __init__(self,toplevel):
        self.frame=Frame(toplevel)
        self.frame.pack()
        self.frame2=Frame(toplevel)
        self.frame2.pack()

        self.titulo=Label(self.frame,text="Joselito's Adventure",
                          font=('Verdana','13','bold'))
        self.titulo.pack()


raiz=Tk()
raiz.resizable(width=False, height=False)
#raiz.geometry('{}x{}'.format(600, 600))
Janela(raiz)
raiz.wm_title("Joselito's Adventure")

bckg=PhotoImage(file="img2.gif")
w = bckg.width()
h = bckg.height()
label=Label(raiz, image=bckg)
label.pack()

b01=Button(raiz,text="Sair",width=40, bg='#E4EFF2',command=raiz.destroy )
b01.pack()


raiz.mainloop()
