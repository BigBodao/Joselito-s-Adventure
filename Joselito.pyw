from tkinter import *
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
raiz.geometry('{}x{}'.format(600, 600))
Janela(raiz)
raiz.mainloop()
