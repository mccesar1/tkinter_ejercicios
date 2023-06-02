import fractions
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter


class Usuario():

     def __init__(self, window):
        self.wind = window
        self.wind.title('DAIRYFOX')
        self.wind.geometry('800x500')
        window.columnconfigure(0, weight=1)
        window.columnconfigure(0, weight=2)
            # grid layout for the input frame
        

        frame1 = LabelFrame(self.wind, text='Dairyfox')
        frame1.place_configure(x=10, y=10, width=480, height=480)

        frame2 = LabelFrame(self.wind,)
        frame2.pack(side=RIGHT)

        frame1.columnconfigure(0, weight=1)
        frame2.columnconfigure(0, weight=3)
          #nserie input
        Label(frame1, text='Numero de serie: ').grid(row=1, column=0, sticky=W, padx=10, pady=10)
        self.name = Entry(frame1)
        self.name.grid(row=1, column=1, padx=10, pady=10)
        self.name.focus()

       
        Label(frame1, text='clave de activacion: ').grid(row=2, column=0, sticky=W, padx=10, pady=10)
        self.price = Entry(frame1)
        self.price.grid(row=2, column=1, padx=10, pady=10)

        
        Label(frame1, text='fecha de caducidad: ').grid(row=3, column=0, sticky=W, padx=10, pady=10)
        self.price = Entry(frame1)
        self.price.grid(row=3, column=1, padx=10, pady=10)

        Label(frame1, text='clave de fecha: ').grid(row=4, column=0, sticky=W, padx=10, pady=10)
        self.price = Entry(frame1)
        self.price.grid(row=4, column=1, padx=10, pady=10)

        Label(frame1, text='1-EID 2-SCR: ').grid(row=5, column=0, sticky=W, padx=10, pady=10)
        self.price = Entry(frame1)
        self.price.grid(row=5, column=1, padx=10, pady=10)

        Label(frame1, text='Alerta: ').grid(row=6, column=0, sticky=W, padx=10, pady=10)
        self.price = Entry(frame1)
        self.price.grid(row=6, column=1, padx=10, pady=10)

        img = tkinter.PhotoImage(file="vaca.png")
        lbl_imagen = tkinter.Label(frame1, image=img)
        lbl_imagen.grid(row=7, column=0, columnspan=2)
        btn1=Button(frame2, text='Aceptar', )
        #btn1.pack(side=, padx=10, pady=10)
        btn2= Button(frame2, text='Cancelar', )


if __name__ == '__main__':
      window = Tk()
      application = Usuario(window)
      window.mainloop()
 
