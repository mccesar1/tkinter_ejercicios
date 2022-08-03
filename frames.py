
from distutils.cmd import Command
from tkinter import *

def cambiar_colorRojo():
    frame1.config(bg="red")
def cambiar_colorAzul():
    frame1.config(bg="blue")
def cambiar_colorVerde():
    frame1.config(bg="green")

ventana = Tk()
ventana.title("frames")
ventana.geometry("360x300")


frame1 = Frame(ventana)
frame1.pack(expand=True, fill="both",)
frame1.config(bg="red", cursor="pirate")


frame2 = Frame(ventana)
frame2.pack(expand=True, fill="both",)

redButton =Button(frame1, text="red", fg="red", command=cambiar_colorRojo)
greenButton =Button(frame1, text="green", fg="green", command=cambiar_colorVerde)
blueButton =Button(frame1, text="blue", fg="blue",  command=cambiar_colorAzul)

redButton.place(x=10, y=10, width=100, height=30, )
greenButton.place(x=10, y=50, width=100, height=30, )
blueButton.place(x=10, y=90, width=100, height=30, )



ventana.mainloop()