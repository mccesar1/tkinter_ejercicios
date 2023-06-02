#-----------------Se importan las librerias--------------------------
 
from tkinter import*
from digi.xbee.devices import XBeeDevice

#------------------Se inicializan Variables y puertos-----------------
 
PORT = "COM5"
BAUD_RATE = 9600
device = XBeeDevice(PORT, BAUD_RATE)
 
#------------------- Se crea la pantalla principal--------------------
 
raiz=Tk()
raiz.title("Sistema de Monitoreo de Paneles Solares del SESLab")
raiz.config(bg="orange")
 
miframe=Frame(raiz,width="1200",height="600" )
miframe.pack()
miframe.config(bg="purple")
 
#-----------------Valores por Mostrar en la Pantallas-----------------
 
voltage=StringVar()
 
#--------------- Cuadros donde se muestran datos-----------------------
 
cuadroVisual= Entry(miframe, textvariable=voltage)
cuadroVisual.grid(row=1, column= 1, padx=1, pady=5)
cuadroVisual.config(fg="black",justify="center")
 
cuadroVisual= Entry(miframe, textvariable=voltage)
cuadroVisual.grid(row=2, column= 1, padx=1, pady=5)
cuadroVisual.config(fg="black",justify="center")
 
cuadroVisual= Entry(miframe, textvariable=voltage)
cuadroVisual.grid(row=4, column= 1, padx=1, pady=5)
cuadroVisual.config(fg="black",justify="center")
 
cuadroVisual= Entry(miframe, textvariable=voltage)
cuadroVisual.grid(row=5, column= 1, padx=1, pady=5)
cuadroVisual.config(fg="black",justify="center")
 
cuadroVisual= Entry(miframe, textvariable=voltage)
cuadroVisual.grid(row=6, column= 1, padx=1, pady=5)
cuadroVisual.config(fg="black",justify="center")
 
cuadroVisual= Entry(miframe, textvariable=voltage)
cuadroVisual.grid(row=7, column= 1, padx=1, pady=5)
cuadroVisual.config(fg="black",justify="center")
 
cuadroVisual= Entry(miframe, textvariable=voltage)
cuadroVisual.grid(row=9, column= 1, padx=1, pady=5)
cuadroVisual.config(fg="black",justify="center")
 
#----------------Cuadros donde esta el Texto "Voltage de Panel 1"--------
 
miLabel=Label(miframe, text="Sistema de monitoreo de Paneles del SESLab", font=18)
miLabel.grid(row=0, column= 0, padx= 5, pady=5, columnspan= 2)
 
nombrePanel=Label(miframe, text="Fecha de medición : ")
nombrePanel.grid(row=1, column= 0, padx= 2, pady=5)
 
nombrePanel=Label(miframe, text="Hora de medición : ")
nombrePanel.grid(row=2, column= 0, padx= 2, pady=5)
 
nombrePanel=Label(miframe, text="Voltage de Panel 1 : ")
nombrePanel.grid(row=4, column= 0, padx= 2, pady=5)
 
nombrePanel=Label(miframe, text="Voltage de Panel 2 : ")
nombrePanel.grid(row=5, column= 0, padx= 2, pady=5)
 
nombrePanel=Label(miframe, text="Voltage de Panel 3 : ")
nombrePanel.grid(row=6, column= 0, padx= 2, pady=5)
 
nombrePanel=Label(miframe, text="Promedio : ")
nombrePanel.grid(row=7, column= 0, padx= 2, pady=5)
 
nombrePanel=Label(miframe, text="Panel con Menor Voltaje : ")
nombrePanel.grid(row=9, column= 0, padx= 2, pady=5)
 
#----------------Función que manda un mensaje Broadcast a Xbees---------
 
def codigoIniciar():
    device.open()
    device.flush_queues()
    DATA_TO_SEND = "Hola XBee!"
    device.send_data_broadcast(DATA_TO_SEND)
 
#----------------Boton que llama a la función CodigoIniciar--------------
 
botonEnvio=Button(raiz, text="Iniciar " ,command=codigoIniciar)
botonEnvio.pack()
 
#----------------Loop de la ventana  --------------
 
raiz.mainloop()