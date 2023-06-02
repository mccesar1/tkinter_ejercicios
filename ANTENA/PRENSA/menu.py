
from PIL import ImageTk, Image 
from tkinter import *
from tkinter import ttk
from tkinter import ttk
import binascii
import csv
import os
import threading
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import socket
import sqlite3
from tkinter import font
import openpyxl
from PIL import ImageTk, Image  


class Principal1:


  def __init__(self, ws):
        self.ws = ws
        self.ws.title('Agroplus')
        self.ws.attributes("-fullscreen", True)
        self.ws.configure(background='black')

        self.widgets()


        s = ttk.Style()

    
#####funcion para crear widgets##################################################################################################################################




  def widgets(self):
    

        path = "BOVYFOX.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(self.ws, image=img, bg='black')
        panel.photo = img
        panel.place(x=370, y=300)
        

        btn9=self.boton = Button(self.ws, text='Entrar', command=self.ws.destroy)
        btn9.config(width=6, height=1, font=('Arial', 48), bg='#a8d5e5', fg='black')
        btn9.place(x=1050, y=610)
        

#####FRAME DE LA IZQUIERDA##################################################################################################################################
        


if __name__ == '__main__':
    ws = Tk()
    application = Principal1(ws)
    ws.mainloop()