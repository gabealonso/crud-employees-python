from tkinter import *
from tkinter import ttk

import sqlite3

class Persona:

    dbname = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Empleados')

        #creamos un container
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
        
        Label(Frame, text='Activo:').grid(row = 4, column= 0)
        self.area = Entry(Frame)
        self.area.grid(row= 4, column=1)
                
        Label(Frame, text='Suspendido:').grid(row = 5, column= 0)
        self.area = Entry(Frame)
        self.area.grid(row= 5, column=1)
        
        #Boton
        ttk.Button(Frame, text='Agregar nuevo empleado').grid(row=5, columnspan= 2, sticky=W + E)
        #Tabla
        self.tree = ttk.Treeview(height=10, columns=("Nombre","Apellido","DNI","Activo", "Suspendido"))
        self.tree.grid(row= 5)
        self.tree.heading('#0', text="Nombre")
        self.tree.heading('#1', text="Apellido")
        self.tree.heading('#2', text="DNI")
        self.tree.heading('#3', text="Activo")
        self.tree.heading('#4', text="Suspendido")
        self.get_empleados()

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.dbname) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_empleados(self):
       #limpiar la tabla
       records = self.tree.get_children()
       for element in records:
           self.tree.delete(element)
       #consulta    
       query = 'SELECT nombre,apellido,dni,activo,suspendido FROM empleados ORDER BY nombre DESC'
       db_rows  = self.run_query(query)
       for row in db_rows:
           print(row[0], row[1],row[2],row[3],row[4])
           self.tree.insert(parent='', index=0, values=(row[0],row[1],row[2],row[3],row[4]) )
           

       
if __name__  == '__main__':
    window = Tk()
    aplication = Persona(window)
    window.mainloop()


