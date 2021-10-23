from tkinter import *
import sqlite3
from tkinter import ttk

def app():
    global ventana_login
    ventana_login = Tk()
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
#    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
#    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
#    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()
    ventana_login.mainloop()

def verifica_login():
    if entrada_login_usuario.get() == "user" and entrada_login_clave.get() == "123": ## falta conexion a la DB
        ingresar_pantalla_principal()
    else:
        print("nada que ver la psswrd")

## Menu principal

def ingresar_pantalla_principal():
    global ventana_gestor
    ventana_gestor = Toplevel(ventana_login)
    ventana_gestor.geometry("300x250")
    ventana_gestor.grab_set()
    ventana_gestor.title("Gestos de Empleados v1.0.0 BETA")
    pestas_color="DarkGrey"
    Label(ventana_gestor, text="Menu principal", bg="LightGreen", width="300", height="2").pack()
    Button(ventana_gestor, text="Agregar administrador", height="2", width="30", bg=pestas_color, command = registrar_admin).pack()
    Button(ventana_gestor, text="Gestionar empleados", height="2", width="30", bg=pestas_color, command = gestionar_empleados).pack()
    Button(ventana_gestor, text="Desactivar empleado", height="2", width="30", bg=pestas_color, command = suspender_empleados).pack()

## Pantalla agregar admin    

def registrar_admin():
    global ventana_registrar_admin
    ventana_registrar_admin = Toplevel(ventana_gestor)
    ventana_registrar_admin.geometry("300x250")
    ventana_registrar_admin.grab_set()
    ventana_registrar_admin.title("Registrar administrador")
    ## agregar un campo user, otro password y un boton de registro
    global verifica_usuario_nuevo
    global verifica_clave_nuevo
 
    verifica_usuario_nuevo = StringVar()
    verifica_clave_nuevo = StringVar()
 
    global entrada_registro_usuario
    global entrada_registro_clave
 
    Label(ventana_registrar_admin, text="Introduzca nombre de usuario y contraseña para administrador nuevo").pack()
    Label(ventana_registrar_admin, text="Nombre usuario * ").pack()
    entrada_registro_usuario = Entry(ventana_registrar_admin, textvariable=verifica_usuario_nuevo)
    entrada_registro_usuario.pack()
    Label(ventana_registrar_admin, text="Contraseña * ").pack()
    entrada_registro_clave = Entry(ventana_registrar_admin, textvariable=verifica_clave_nuevo, show= '*')
    entrada_registro_clave.pack()
    Button(ventana_registrar_admin, text="Registrar", width=10, height=1, command = registrar).pack()

## funcion para registrar nuevo administrador

def registrar():
    print("registrado")

def gestionar_empleados():
    global ventana_gestionar_empleados
    ventana_gestionar_empleados = Toplevel(ventana_gestor)
    ventana_gestionar_empleados.geometry("1250x640")
    ventana_gestionar_empleados.grab_set()
    ventana_gestionar_empleados.title("Agregar empleado")
        
    Label(ventana_gestionar_empleados, text="Nombre ").pack()
    entrada_nombre_empleado = Entry(ventana_gestionar_empleados)
    entrada_nombre_empleado.pack()

    Label(ventana_gestionar_empleados, text="Apellido").pack()
    entrada_apellido_empleado = Entry(ventana_gestionar_empleados)
    entrada_apellido_empleado.pack()

    Label(ventana_gestionar_empleados, text="DNI").pack()
    entrada_dni_empleado = Entry(ventana_gestionar_empleados)
    entrada_dni_empleado.pack()

    Button(ventana_gestionar_empleados, text="Desactivar empleado", height="2", width="30", command = agregar_empleado).pack()
    tree = ttk.Treeview(height=10, columns=("Nombre","Apellido","DNI","Activo", "Suspendido"))
    tree.heading('#0', text="Nombre")
    tree.heading('#1', text="Apellido")
    tree.heading('#2', text="DNI")
    tree.heading('#3', text="Activo")
    tree.heading('#4', text="Suspendido")


def agregar_empleado():
    print("ASD")


    # agregar el form para agregar empleados y la tabla para buscar empleados

def suspender_empleados():
    global ventana_suspender_empleados
    ventana_suspender_empleados = Toplevel(ventana_gestor)
    ventana_suspender_empleados.geometry("300x250")
    ventana_suspender_empleados.grab_set()
    ventana_suspender_empleados.title("Suspender empleado")
    # agregar un boton para desactivar y un input para el ID del empleado
    global id_usuario
 
    id_usuario = StringVar()
 
    global entrada_id_usuario
 
    Label(ventana_suspender_empleados, text="ID del empleado * ").pack()
    entrada_id_usuario = Entry(ventana_suspender_empleados, textvariable=id_usuario)
    entrada_id_usuario.pack()
    Button(ventana_suspender_empleados, text="Desactivar", width=10, height=1, command = desactivar).pack()

## funcion para desactivar empleado

def desactivar():
    print("desactivado")


app()