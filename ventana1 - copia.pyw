
from cProfile import label
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from cairo import FontWeight 
import tkinter.filedialog as fd


class Principal:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Agroplus')
        self.wind.geometry('1090x460')

        window.configure(background='#063970')

        n_rows =9
        n_columns =3
        for i in range(n_rows):
            window.grid_rowconfigure(i,  weight =1)
        for i in range(n_columns):
            window.grid_columnconfigure(i,  weight =1)
        
        frame = LabelFrame(self.wind, text='Registrar Productos').grid(row=0, column=0, columnspan=3, padx=10, pady=10)
       # Label(frame, text="Nombre:").grid(pady=5,padx=5, row=0, column=0, sticky=W)
        ttk.Button(frame, text='OK', ).grid(row=0,column=0, sticky=W+E, ipady=9, ipadx=120,pady=5)
        btn= Text(frame, width=10, height=20).grid(row=1,column=0, sticky=W+E, ipady=9, ipadx=120, rowspan=6)
      
        #ttk.Entry(frame, width=20).grid(row=2,column=0, sticky=W+E, ipady=240, ipadx=120, padx=0, pady=5, columnspan=1, )
        ttk.Button(frame, text='CONECTAR ANTENA', ).grid(row=9,column=0, sticky=W+E, ipady=9, ipadx=120, pady=5)

        
        #ttk.Label(frame, text='LEIDAS', ).grid(row=0,column=1, sticky=W+E, ipady=9, ipadx=120, padx=5,)
        ttk.Button(frame, text='SALIR', command=window.destroy).grid(row=9,column=1, sticky=W+E, ipady=9, ipadx=120, padx=40)

        ttk.Button(frame, text='CONECTAR', ).grid(row=1,column=2, ipady=9, ipadx=120, pady=1, padx=5)
        ttk.Button(frame, text='DESCONECTAR', ).grid(row=2,column=2, ipady=9, ipadx=120, pady=1, padx=5)
        ttk.Button(frame, text='GRABAR', command=self.guardar_contenido ).grid(row=3,column=2,  ipady=9, ipadx=120, pady=1, padx=5)
        ttk.Button(frame, text='XLS', ).grid(row=4,column=2, ipady=9, ipadx=120, pady=1, padx=5)
        ttk.Button(frame, text='RESPALDO', ).grid(row=5,column=2,  ipady=9, ipadx=120, pady=1, padx=5)

        Label(frame, text='LEIDAS:', bg="#063970", fg="white", font=("Arial", 25)).grid(row=0, column=1,  ipady=9, ipadx=120)
        Entry(frame, width=10, bg="white", fg="white").grid(row=1, column=1,  ipady=9, ipadx=120)
        Label(frame, text='TOTAL:', bg="#063970", fg="white", font=("Arial", 25)).grid(row=2, column=1,  ipady=9, ipadx=120)
        Entry(frame, width=10, bg="white", fg="white").grid(row=3, column=1,ipady=9, ipadx=120)
        Label(frame, text='USB:', bg="#063970", fg="white", font=("Arial", 25)).grid(row=4, column=1,  ipady=9, ipadx=120)
        Entry(frame, width=10, bg="white", fg="white").grid(row=5, column=1,  ipady=9, ipadx=120)
        #lbl1=ttk.Label(frame, text='LEIDAS:').grid(row=0,column=1, sticky=W, padx=10, pady=10)
        #lbl1.config(background='#063970')
    
    def guardar_contenido(self):
        archivo = fd.asksaveasfile(mode="w", defaultextension=".txt")
        if archivo is not None:
            archivo.write(self.txt_contenido.get(1.0, tk.END))
            archivo.close()
        else:
            pass
       
        #btnSalir = Button(window, text="Salir", command=window.destroy)
        #btnSalir.configure(width=10, height=2)
       # btnSalir.place(x=800, y=550)

    
        
        





if __name__ == '__main__':
     window = Tk()
     application = Principal(window)
     window.mainloop()
