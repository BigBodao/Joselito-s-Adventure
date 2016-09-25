from tkinter import *

root = Tk()

photo = PhotoImage(file="img2.gif")
label = Label(root, image=photo)
label.pack()

root.mainloop()
