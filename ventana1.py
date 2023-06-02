
from cProfile import label
from sqlite3 import Row
from tkinter import *
from tkinter import ttk



import tkinter.font as font
from tkinter.tix import COLUMN
#from cairo import FontWeight
import tkinter.filedialog as fd
import pywin32_system32 as win32
import serial
import serial.tools.list_ports

 
class Principal:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Agroplus')
        self.wind.geometry('1090x460')

        window.configure(background='#063970')
    #
        #funcion para que sea responsive el tamaño de la ventana
        n_rows =9
        n_columns =3

        
        for i in range(n_rows):
            window.grid_rowconfigure(i,  weight =1)
        for i in range(n_columns):
            window.grid_columnconfigure(i,  weight =1,)
#----------------------------------------------------------------------------------------------------------------------
        def serial_ports( ):
            return [p.device for p in serial.tools.list_ports.comports()]

        def on_select( event=None ):

            # get selection from event
            print("event.widget:", event.widget.get())

            # or get selection directly from combobox
            print("comboboxes: ", ttk.Combobox.get())

        # label0 = ttk.Label(window, text="Select the COM port that the device is plugged in: ")
        # label0.config(font=("TkDefaultFont", 8))
        # label0.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.5)

        # cb = ttk.Combobox(window, values=serial_ports())
        # cb.place(relx=0.5, rely=0.5, anchor='center')
        # assign function to combobox
        # cb.bind('<<ComboboxSelected>>', on_select)
  #################################################################################################

        frame = LabelFrame(self.wind, text='Registrar Productos').grid(row=0, column=0,)
       # Label(frame, text="Nombre:").grid(pady=5,padx=5, row=0, column=0, sticky=W)
        ttk.Button(frame, text='OK', ).grid(row=0,column=0, sticky=W+E, ipady=9, ipadx=120,pady=5, padx=5)
        btn= Text(frame, width=10, height=20).grid(row=1,column=0, sticky=W+E, ipady=9, ipadx=120, rowspan=6, padx=5)
      
        #ttk.Entry(frame, width=20).grid(row=2,column=0, sticky=W+E, ipady=240, ipadx=120, padx=0, pady=5, columnspan=1, )
        ttk.Button(frame, text='CONECTAR ANTENA', ).grid(row=9,column=0, sticky=W+E, ipady=9, ipadx=120, pady=5, padx=5)

        
        #ttk.Label(frame, text='LEIDAS', ).grid(row=0,column=1, sticky=W+E, ipady=9, ipadx=120, padx=5,)
        ttk.Button(frame, text='SALIR', command=window.destroy).grid(row=9,column=2,  ipady=9, ipadx=20, padx=40)

        ttk.Button(frame, text='   CONECTAR   ', ).grid(row=1,column=2, ipady=9, ipadx=20, pady=1, padx=5)
        ttk.Button(frame, text='DESCONECTAR', ).grid(row=2,column=2, ipady=9, ipadx=20, pady=1, padx=5)
        ttk.Button(frame, text='    GRABAR      ', command=self.guardar_contenido ).grid(row=3,column=2,  ipady=9, ipadx=20, pady=1, padx=5)
        ttk.Button(frame, text= '          XLS        ', ).grid(row=4,column=2, ipady=9, ipadx=20, pady=1, padx=5)
        ttk.Button(frame, text='     RESPALDO   ', ).grid(row=5,column=2,  ipady=9, ipadx=20, pady=1, padx=5)

        Label(frame, text='LEIDAS:', bg="#063970", fg="white", font=("Arial", 25)).grid(row=0, column=1,  ipady=2, ipadx=20, padx=5, pady=5)
        Entry(frame, width=10, bg="white", fg="white").grid(row=1, column=1,  ipady=9, ipadx=20)
        Label(frame, text='TOTAL:', bg="#063970", fg="white", font=("Arial", 25)).grid(row=2, column=1,  ipady=9, ipadx=120)
        Entry(frame, width=10, bg="white", fg="white").grid(row=3, column=1,ipady=9, ipadx=20)
        Label(frame, text='USB:', bg="#063970", fg="white", font=("Arial", 25)).grid(row=4, column=1,  ipady=9, ipadx=120)
       #(frame, width=10, bg="white", fg="white").grid(row=5, column=1,  ipady=9, ipadx=20)
        cb = ttk.Combobox(window, values=serial_ports())
        cb.grid(row=5, column=1, ipady=9, ipadx=20)
        cb.bind('<<ComboboxSelected>>', on_select)
        #lbl1=ttk.Label(frame, text='LEIDAS:').grid(row=0,column=1, sticky=W, padx=10, pady=10)
        #lbl1.config(background='#063970')
    
    def guardar_contenido(self):
        archivo = fd.asksaveasfile(mode="w", defaultextension=".txt")
        if archivo is not None:
            archivo.write(self.txt_contenido.get(1.0, ttk.END))
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
