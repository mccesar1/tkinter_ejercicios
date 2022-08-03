from tkinter import *


class MiVentana(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=300, height=300)
        self.master= master
        self.pack()
        self.createWidgets()


    def sumar(self) :   
        n1=int(self.txt1.get())
        n2=int(self.txt2.get())
        resultado=float(n1)+float(n2)
        self.txt3.delete(0,END) # borra el contenido de la caja de texto
        self.txt3.insert(0,resultado) 

    def createWidgets(self):
        self.lb1 = Label(self, text="primer numero")
        #lbl.place(x=10, y=50, width=100, height=30)
        self.txt1 = Entry(self, bg="pink", fg="white")
        #txt1.place(x=120, y=50, width=100, height=30)
        self.lb2 = Label(self, text="segundo numero")
        #lb2.place(x=10, y=90, width=100, height=30)
        self.txt2 = Entry(self, bg="pink", fg="white")
        #txt2.place(x=120, y=90, width=100, height=30)
        self.lb3 = Label(self, text="resultado ")
        #lb3.place(x=10, y=130, width=100, height=30)
        self.txt3 = Entry(self, bg="pink", fg="white", )
        #txt3.place(x=120, y=130, width=100, height=30)
        self.btnsumar = Button(self, text="sumar", command=self.sumar)
        #btnsumar.place(x=10, y=170, width=100, height=30)
        #lbl.pack() #pack es para que se vea en la self

        self.lb1.grid(row=0, column=0, padx=10, pady=10, sticky=W, ipady=6) 
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.lb2.grid(row=1, column=0, padx=10, pady=10, sticky=W, ipady=6)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.lb3.grid(row=2, column=0, padx=10, pady=10, sticky=W, ipady=6)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.btnsumar.grid(row=1, column=2, padx=10, pady=10, ipady=4, ipadx=6)

ventana = Tk()
ventana.wm_title("sumarPOO")
app = MiVentana(ventana)
app.mainloop()