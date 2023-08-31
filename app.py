import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Aplicación Básica con Tkinter')
        self.geometry('400x200')
        
        etiqueta = tk.Label(self, text='Hola, mundo!')
        etiqueta.pack(padx=10, pady=10)
        
        boton = tk.Button(self, text='Salir', command=self.destroy)
        boton.pack(padx=10, pady=10)

if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()
