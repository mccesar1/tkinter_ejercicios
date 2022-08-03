
from tkinter import *
from tkinter import ttk

import sqlite3
from tkinter import messagebox 

class Product:

    db_name='database.db'


    def __init__(self, window):
        self.wind = window
        self.wind.title('Productos')

        frame = LabelFrame(self.wind, text='Registrar Productos').grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        #name input
        Label(frame, text='Nombre: ').grid(row=1, column=0, sticky=W, padx=10, pady=10)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1, padx=10, pady=10)
        self.name.focus()

        #price input
        Label(frame, text='Precio: ').grid(row=2, column=0, sticky=W, padx=10, pady=10)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1, padx=10, pady=10)

        #btn agregar producto
        Button(frame, text='Agregar Producto', command=self.add_product).grid(row=3, columnspan=2, padx=10, pady=10)
        #btn eliminar producto
        Button(frame, text='Eliminar Producto', command=self.delete_product).grid(row=4, columnspan=2, padx=10, pady=10)


        #table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=6, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Precio',  anchor=CENTER)

        self.get_products()

    def conexion(self, query, parameters=()):
      with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
        return result
    
    def get_products(self):
        #cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #getting data
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.conexion(query)
        #inserting data
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    def add_product(self):
        if self.name.get() == '' or self.price.get() == '':
            messagebox.showerror('Error', 'Todos los campos son obligatorios')
            return
        query = 'INSERT INTO product VALUES(NULL, ?, ?)'
        parameters = (self.name.get(), self.price.get())
        
        self.conexion(query, parameters)
        self.get_products()
        
        messagebox.showinfo('Producto agregado', 'El producto {} ha sido agregado'.format(self.name.get()))
        self.name.delete(0, END)
        self.price.delete(0, END)
        self.name.focus()
    
    def delete_product(self):
        self.tree.delete(self.tree.selection())
        query = 'DELETE FROM product WHERE name = ?'
        parameters = (self.name.get(),)
        self.conexion(query, parameters)
        self.get_products()
        messagebox.showinfo('Producto eliminado', 'El producto ha sido eliminado')

if __name__ == '__main__':
     window = Tk()
     application = Product(window)
     window.mainloop()

    