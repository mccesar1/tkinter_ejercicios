from tkinter import *
from tkinter import ttk

class App(Frame):

    def __init__(self, master=None):

        super().__init__(master, width=300, height=300)
        self.master= master
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.lb1 = Label(self, text="DATO 1")
        #lbl.place(x=10, y=50, width=100, height=30)
        self.txt1 = Entry(self, bg="white", fg="white")
        #txt1.place(x=120, y=50, width=100, height=30)
        self.lb2 = Label(self, text="DATO 2")
        #lb2.place(x=10, y=90, width=100, height=30)
        self.txt2 = Entry(self, bg="white", fg="white")

        self.lb1.grid(row=0, column=0, padx=0, pady=10, sticky=W, ipady=6) 
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.lb2.grid(row=1, column=0, padx=10, pady=10, sticky=W, ipady=6)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)


        self.btnSalir = Button(self, text="Salir", command=ventana.destroy)
        self.btnSalir.grid(row=2, column=2, padx=10, pady=10, ipady=4, ipadx=6)



ventana = Tk()
ventana.wm_title("sumarPOO")
app = App(ventana)
app.mainloop()
 