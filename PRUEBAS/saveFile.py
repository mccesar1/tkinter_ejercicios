import tkinter as tk
import tkinter.filedialog as fd



class AlmacenamientoContenido(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.inicializarVentana()


    def inicializarVentana(self):
        self.title("Almacenamiento de contenido")
        self.geometry("400x400")    

        self.txt_contenido = tk.Text(self, width=30, height=10)

        btn_guardar = tk.Button(self, text="Guardar", command=self.guardar_contenido)
        btn_guardar.pack(side=tk.BOTTOM)

    
    def guardar_contenido(self):
        archivo = fd.asksaveasfile(mode="w", defaultextension=".txt")
        if archivo is not None:
            archivo.write(self.txt_contenido.get(1.0, tk.END))
            archivo.close()
        else:
            pass

def main():
    app = AlmacenamientoContenido()
    app.mainloop()

if __name__ == "__main__":
    main()