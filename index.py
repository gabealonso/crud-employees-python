from tkinter import *
#diseñar toda la interfaz
from tkinter import ttk
#conectar a la db
import sqlite3


class Persona:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Empleados')

        #crear un container
        Frame = LabelFrame(self.wind, text= 'Empleados')
        Frame.grid(row = 0, column= 0, columnspan= 3, pady=20 )
        #input
        Label(Frame, text='Nombre:').grid(row = 1, column= 0)
        self.name = Entry(Frame)
        self.name.grid(row= 1, column=1)
        
        Label(Frame, text='Apellido:').grid(row = 2, column= 0)
        self.apellido = Entry(Frame)
        self.apellido.grid(row= 2, column=1)
        
        Label(Frame, text='DNI:').grid(row = 3, column= 0)
        self.dni = Entry(Frame)
        self.dni.grid(row= 3, column=1)
        
        Label(Frame, text='Area:').grid(row = 4, column= 0)
        self.area = Entry(Frame)
        self.area.grid(row= 4, column=1)
        
        #Boton
        ttk.Button(Frame, text='Agregar nuevo empleado').grid(row=5, columnspan= 2, sticky=W + E)
        #Tabla
        self.tree = ttk.Treeview(height=10, columns=("Apellido","DNI","Area"))
        self.tree.grid(row= 6)
        self.tree.heading('#0', text="Nombre")
        self.tree.heading('#1', text="Apellido")
        self.tree.heading('#2', text="DNI")
        self.tree.heading('#3', text="Area")
if __name__  == '__main__':
    window = Tk()
    aplication = Persona(window)
    window.mainloop()


