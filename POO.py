from tkinter import *


class Aplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.helloButton = Button(self, text='Hello', command=self.hello)
        self.helloButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        print('Hello, world!')

ventana = Tk()
app = Aplication(ventana)
app.mainloop()


