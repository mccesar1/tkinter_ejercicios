from distutils.cmd import Command
from tkinter import *


def mifuncion():
    print("Hola cesar")

def sumar() :   
    n1=int(txt1.get())
    n2=int(txt2.get())
    resultado=float(n1)+float(n2)
    txt3.delete(0,END) # borra el contenido de la caja de texto
    txt3.insert(0,resultado)

ventana = Tk()
ventana.title("Hola mundo")
ventana.geometry("360x300") #ancho x alto
ventana.config(bg="white") #color de fondo


lb1 = Label(ventana, text="primer numero")
#lbl.place(x=10, y=50, width=100, height=30)

txt1 = Entry(ventana, bg="pink", fg="white")
#txt1.place(x=120, y=50, width=100, height=30)


lb2 = Label(ventana, text="segundo numero")
#lb2.place(x=10, y=90, width=100, height=30)

txt2 = Entry(ventana, bg="pink", fg="white")
#txt2.place(x=120, y=90, width=100, height=30)


lb3 = Label(ventana, text="resultado ")
#lb3.place(x=10, y=130, width=100, height=30)

txt3 = Entry(ventana, bg="pink", fg="white", )
#txt3.place(x=120, y=130, width=100, height=30)

btnsumar = Button(ventana, text="sumar", command=sumar)
#btnsumar.place(x=10, y=170, width=100, height=30)
#lbl.pack() #pack es para que se vea en la ventana

lb1.grid(row=0, column=0, padx=10, pady=10, sticky=W, ipady=6) 
txt1.grid(row=0, column=1, padx=10, pady=10)
lb2.grid(row=1, column=0, padx=10, pady=10, sticky=W, ipady=6)
txt2.grid(row=1, column=1, padx=10, pady=10)
lb3.grid(row=2, column=0, padx=10, pady=10, sticky=W, ipady=6)
txt3.grid(row=2, column=1, padx=10, pady=10)
btnsumar.grid(row=1, column=2, padx=10, pady=10, ipady=4, ipadx=6)







# btn = Button(ventana, text="Salir", command=mifuncion)
# btn.pack()
# btn.config(bg="red") #color de fondo
# btn.place(relx=0.9, rely=0.9) #posicion relativa
#btn.place( x=100, y=100) #posicion absoluta

ventana.mainloop() #para que se ejecute