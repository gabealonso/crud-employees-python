from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from hashlib import sha256

ColorBotones = '#cdcdb4'
BackGroundColor = '#eae2b7'
HeadingColor = '#fcbf49'

dbname = 'database.db'

class Empleado():
    def __init__(self, nombre, apellido, dni, area):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.area = area

    def __str__(self):
        cad = "Nombre: {}, Apellido {}, DNI {}, Area {}"
        return cad.format(self.nombre, self.apellido, self.dni, self.area)

def run_query(query, parameters = ()):
    with sqlite3.connect(dbname) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

## aplicacion

def app():
    
    global ventana_login
    ventana_login = Tk()
    ventana_login.iconbitmap('icon.ico')
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("350x300")
    ventana_login.configure(bg=BackGroundColor)
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña", bg=BackGroundColor, padx=20, pady=20).pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ", bg=BackGroundColor).pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="Contraseña * ", bg=BackGroundColor, padx=20, pady=2).pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Button(ventana_login, text="Acceder", width=10, height=1, bg=ColorBotones, command = verifica_login).pack()
    ventana_login.mainloop()

## verificar login

def verifica_login():
    user = entrada_login_usuario.get()
    password = entrada_login_clave.get()
    login = [user, sha256(password.encode('utf-8')).hexdigest()]
    query = 'SELECT usuario, clave FROM usuarios_rrhh WHERE usuario = ? AND clave = ?;'
    db_users = run_query(query, login)
    if(login[0] != '' and login[1] != ''):
        if db_users.fetchall():
            ingresar_pantalla_principal()
        else:
             messagebox.showinfo("Clave y/o usuario incorrecto","El usuario o clave que esta intentando ingresar son incorrectos")
    else:
       messagebox.showinfo("Campos requeridos","Todos los campos son requeridos")


## Menu principal

def ingresar_pantalla_principal():
    global ventana_gestor
    ventana_gestor = Toplevel(ventana_login)
    ventana_gestor.geometry("350x300")
    ventana_gestor.iconbitmap('icon.ico')
    ventana_gestor.configure(bg=BackGroundColor)
    ventana_gestor.grab_set()
    ventana_gestor.title("Gestor de Empleados v1.0.0 BETA")
    Label(ventana_gestor, text="Menu principal", bg=HeadingColor, width="300", height="2").pack()
    Button(ventana_gestor, text="Agregar administrador", height="2", width="30", bg=ColorBotones, command = registrar_admin).pack()
    Button(ventana_gestor, text="Agregar empleados", height="2", width="30", bg=ColorBotones, command = agregar_empleados).pack()
    Button(ventana_gestor, text="Modificar empleado", height="2", width="30", bg=ColorBotones, command = modificar_empleados).pack()
    Button(ventana_gestor, text="Suspender o Activar empleado", height="2", width="30", bg=ColorBotones,  command = suspender_activar_empleados).pack()

## Pantalla agregar admin    

def registrar_admin():
    global ventana_registrar_admin
    ventana_registrar_admin = Toplevel(ventana_gestor)
    ventana_registrar_admin.geometry("500x250")
    ventana_registrar_admin.iconbitmap('icon.ico')
    ventana_registrar_admin.configure(bg=BackGroundColor)
    ventana_registrar_admin.grab_set()
    ventana_registrar_admin.title("Registrar administrador")
    Label(ventana_registrar_admin, text="Registrar administrador", bg=HeadingColor, width="300", height="2").pack()
    global verifica_usuario_nuevo
    global verifica_clave_nuevo
 
    verifica_usuario_nuevo = StringVar()
    verifica_clave_nuevo = StringVar()
 
    global entrada_registro_usuario
    global entrada_registro_clave
 
    Label(ventana_registrar_admin, text="Introduzca nombre de usuario y contraseña para administrador nuevo", bg=BackGroundColor).pack()
    Label(ventana_registrar_admin, text="Nombre usuario * ", bg=BackGroundColor).pack()
    entrada_registro_usuario = Entry(ventana_registrar_admin, textvariable=verifica_usuario_nuevo)
    entrada_registro_usuario.pack()
    Label(ventana_registrar_admin, text="Contraseña * ", bg=BackGroundColor).pack()
    entrada_registro_clave = Entry(ventana_registrar_admin, textvariable=verifica_clave_nuevo, show= '*')
    entrada_registro_clave.pack()
    Button(ventana_registrar_admin, text="Registrar", width=10, height=1, bg=ColorBotones, command = registrar).pack()

## funcion para registrar nuevo administrador

def registrar():
    # validacion
    userNuevo = entrada_registro_usuario.get()
    passwordNueva = entrada_registro_clave.get()
    registerParameters = [userNuevo, passwordNueva]
    if (registerParameters[0] != '' and registerParameters[1] != ''):
        query = 'SELECT usuario FROM usuarios_rrhh WHERE usuario = ?;'
        db_users = run_query(query, (registerParameters[0],))
        if db_users.fetchall():
            messagebox.showinfo("Usuario registrado","El nombre de usuario ya se encuentra registrado")
        else:
            query = 'INSERT INTO usuarios_rrhh VALUES(NULL, ?, ?)'
            registerParameters = [userNuevo, sha256(passwordNueva.encode('utf-8')).hexdigest()] ## se pasa el hash aca para poder validar
            run_query(query, registerParameters)
            messagebox.showinfo("Registro exitoso","El usuario fue registrado correctamente")
    else:
        messagebox.showinfo("Campos requeridos","Todos los campos son requeridos")

## pantalla modificar empleados

def modificar_empleados():
    global ventana_modificar_empleados
    ventana_modificar_empleados = Toplevel(ventana_gestor)
    ventana_modificar_empleados.geometry("500x400")
    ventana_modificar_empleados.iconbitmap('icon.ico')
    ventana_modificar_empleados.configure(bg=BackGroundColor)
    ventana_modificar_empleados.grab_set()
    ventana_modificar_empleados.title("Modificar empleado")

    Label(ventana_modificar_empleados, text="Modificar empleado", bg=HeadingColor, width="300", height="2").pack()

    global entrada_dni_empleado
    global entrada_dni_nuevo_empleado
    global entrada_nombre_empleado
    global entrada_apellido_empleado
    global entrada_area_empleado

    Label(ventana_modificar_empleados, text="DNI del empleado a modificar * ", bg=BackGroundColor).pack()
    entrada_dni_empleado = Entry(ventana_modificar_empleados)
    entrada_dni_empleado.pack()

    Label(ventana_modificar_empleados, text="Nuevo DNI", bg=BackGroundColor).pack()
    entrada_dni_nuevo_empleado = Entry(ventana_modificar_empleados)
    entrada_dni_nuevo_empleado.pack()

    Label(ventana_modificar_empleados, text="Nombre ", bg=BackGroundColor).pack()
    entrada_nombre_empleado = Entry(ventana_modificar_empleados)
    entrada_nombre_empleado.pack()

    Label(ventana_modificar_empleados, text="Apellido", bg=BackGroundColor).pack()
    entrada_apellido_empleado = Entry(ventana_modificar_empleados)
    entrada_apellido_empleado.pack()

    Label(ventana_modificar_empleados, text="Area", bg=BackGroundColor).pack()
    entrada_area_empleado = Entry(ventana_modificar_empleados)
    entrada_area_empleado.pack()

    Button(ventana_modificar_empleados, text="Modificar empleado", height="2", width="30", bg=ColorBotones, command = modificar_empleado).pack()

## funcion para modificar empleado

def modificar_empleado():
    dni_empleado = entrada_dni_empleado.get()
    dni_nuevo = entrada_dni_nuevo_empleado.get()
    nombre = entrada_nombre_empleado.get()
    apellido = entrada_apellido_empleado.get()
    area = entrada_area_empleado.get()
    nuevosValores = [nombre, apellido, dni_nuevo, area, dni_empleado]
    # validacion dni empleado
    if(nuevosValores[0] != '' and nuevosValores[1] != '' and nuevosValores[2] != '' and nuevosValores[3] != '' ):
        query = 'SELECT dni FROM empleados WHERE dni = ?'
        db_empleados = run_query(query, (dni_empleado,))
        if db_empleados.fetchall():
            # modificacion de empleado
            query = 'UPDATE empleados SET nombre = ?, apellido = ?, dni = ?, area = ? WHERE dni = ?'
            db_empleados = run_query(query, nuevosValores)
            messagebox.showinfo("Modificado exitosamente","El empleado se ha modificado correctamente")
        else:
            messagebox.showinfo("Error en la modificacion","Empleado no encontrado")
    else:
        messagebox.showinfo("Campos requeridos","Todos los campos son requeridos")
        

# pantalla agregar empleados

def agregar_empleados():
    global ventana_agregar_empleados
    ventana_agregar_empleados = Toplevel(ventana_gestor)
    ventana_agregar_empleados.geometry("800x500")
    ventana_agregar_empleados.iconbitmap('icon.ico')
    ventana_agregar_empleados.configure(bg=BackGroundColor)
    ventana_agregar_empleados.grab_set()
    ventana_agregar_empleados.title("Agregar empleado")

    Label(ventana_agregar_empleados, text="Agregar empleado", bg=HeadingColor, width="300", height="2").pack()
        
    Label(ventana_agregar_empleados, text="Nombre ", bg=BackGroundColor).pack()
    global entrada_nombre_empleado
    entrada_nombre_empleado = Entry(ventana_agregar_empleados)
    entrada_nombre_empleado.pack()

    Label(ventana_agregar_empleados, text="Apellido", bg=BackGroundColor).pack()
    global entrada_apellido_empleado
    entrada_apellido_empleado = Entry(ventana_agregar_empleados)
    entrada_apellido_empleado.pack()

    Label(ventana_agregar_empleados, text="DNI", bg=BackGroundColor).pack()
    global entrada_dni_empleado
    entrada_dni_empleado = Entry(ventana_agregar_empleados)
    entrada_dni_empleado.pack()

    Label(ventana_agregar_empleados, text="Area", bg=BackGroundColor).pack()
    global entrada_area_empleado
    entrada_area_empleado = Entry(ventana_agregar_empleados)
    entrada_area_empleado.pack()

    Button(ventana_agregar_empleados, text="Agregar empleado", height="2", width="30", bg=ColorBotones, command = agregar_empleado).pack()

    global tv 
    tv = ttk.Treeview(ventana_agregar_empleados)
    tv['columns']=('Nombre', 'Apellido', 'DNI', 'Area')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Nombre', anchor=CENTER, width=80)
    tv.column('Apellido', anchor=CENTER, width=80)
    tv.column('DNI', anchor=CENTER, width=120)
    tv.column('Area', anchor=CENTER, width=120)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Nombre', text='Nombre', anchor=CENTER)
    tv.heading('Apellido', text='Apellido', anchor=CENTER)
    tv.heading('DNI', text='DNI', anchor=CENTER)
    tv.heading('Area', text='Area', anchor=CENTER)

    tv.pack()
    get_empleados()


## funcion para agregar empleados

def agregar_empleado():
    NombreEmpleado = entrada_nombre_empleado.get()
    ApellidoEmpleado = entrada_apellido_empleado.get()
    DniEmpleado = entrada_dni_empleado.get()
    AreaEmpleado =  entrada_area_empleado.get()
    # instancia de clase empleado
    empleadoClase = Empleado(NombreEmpleado, ApellidoEmpleado, DniEmpleado, AreaEmpleado)
    empleadoParameters = [empleadoClase.nombre, empleadoClase.apellido, empleadoClase.dni, empleadoClase.area]
    query = 'SELECT dni FROM empleados WHERE dni = ?;'
    db_empleados = run_query(query, (empleadoParameters[2],))
    if(empleadoParameters[0] != '' and empleadoParameters[1] != '' and empleadoParameters[2] != '' and empleadoParameters[3] != ''):
        if db_empleados.fetchall():
            messagebox.showinfo("DNI existente","El DNI que esta intentando ingresa ya se encuentra registrado")
        else:
            query = 'INSERT into empleados VALUES(null, ?, ?, ?, 0, ?)'
            run_query(query, empleadoParameters)
        get_empleados()
    else:
        messagebox.showinfo("Campos requeridos","Todos los campos son requeridos")

def get_empleados():
    # limpiar la tabla
    records = tv.get_children()
    for element in records:
        tv.delete(element)
    # consulta    
    query = 'SELECT nombre,apellido,dni,area FROM empleados WHERE suspendido = 0 ORDER BY nombre DESC'
    db_rows  = run_query(query)
    for row in db_rows:
        tv.insert(parent='', index=0, values=(row[0], row[1],row[2],row[3]))

## pantalla activar/desactivar empleados

def suspender_activar_empleados():
    global ventana_suspender_activar_empleados
    suspender_activar_empleados = Toplevel(ventana_gestor)
    suspender_activar_empleados.geometry("250x200")
    suspender_activar_empleados.iconbitmap('icon.ico')
    suspender_activar_empleados.configure(bg=BackGroundColor)
    suspender_activar_empleados.grab_set()
    suspender_activar_empleados.title("Suspender/Activar empleado")

    Label(suspender_activar_empleados, text="Suspender/Activar empleado", bg=HeadingColor, width="300", height="2").pack()

    global id_usuario
 
    id_usuario = StringVar()
 
    global entrada_id_usuario
 
    Label(suspender_activar_empleados, text="DNI del empleado * ", bg=BackGroundColor).pack()
    entrada_id_usuario = Entry(suspender_activar_empleados, textvariable=id_usuario)
    entrada_id_usuario.pack()
    Button(suspender_activar_empleados, text="Desactivar", width=10, height=1,bg=ColorBotones, command = desactivar).pack()
    Button(suspender_activar_empleados, text="Activar", width=10, height=1,bg=ColorBotones, command = activar).pack()

## funcion para desactivar empleado

def desactivar():
    dni_empleado = entrada_id_usuario.get()
    # validacion dni empleado
    query = 'SELECT dni FROM empleados WHERE dni = ?'
    db_empleados = run_query(query, (dni_empleado,))
    if (dni_empleado != ''):
        if db_empleados.fetchall():
        # suspension del empleado
            query = 'UPDATE empleados SET suspendido = 1 WHERE dni = ?'
            db_empleados = run_query(query, (dni_empleado,))
            messagebox.showinfo("Empleado suspendido correctamente", "El empleado fue suspendido correctamente")
        else:
            messagebox.showinfo("Empleado no encontrado", "DNI invalido")
    else:
        messagebox.showinfo("Campos requeridos","Todos los campos son requeridos")

## funcion para activar empleado

def activar():
    dni_empleado = entrada_id_usuario.get()
    # validacion id empleado
    query = 'SELECT dni FROM empleados WHERE dni = ?'
    db_empleados = run_query(query, (dni_empleado,))
    if(dni_empleado != ''):
        if db_empleados.fetchall():
        # activacion del empleado
            query = 'UPDATE empleados SET suspendido = 0 WHERE dni = ?'
            db_empleados = run_query(query, (dni_empleado,))
            messagebox.showinfo("Empleado activo", "El empleado se activo correctamente")
        else:
            messagebox.showinfo("Empleado no encontrado", "DNI invalido")
    else:
        messagebox.showinfo("Campos requeridos","Todos los campos son requeridos")

app()