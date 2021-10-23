from tkinter import *
import sqlite3
from tkinter import ttk

def app():
    global ventana_login
    ventana_login = Tk()
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("350x300")
    ventana_login.configure(bg='#eae2b7')
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña", bg='#eae2b7').pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ", bg='#eae2b7').pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="Contraseña * ", bg='#eae2b7').pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
#    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, bg='#fcbf49', command = verifica_login).pack()
    ventana_login.mainloop()

def verifica_login():
    if entrada_login_usuario.get() == "user" and entrada_login_clave.get() == "123": ## falta conexion a la DB
        ingresar_pantalla_principal()
    else:
        print("password incorrecta")

## Menu principal

def ingresar_pantalla_principal():
    global ventana_gestor
    ventana_gestor = Toplevel(ventana_login)
    ventana_gestor.geometry("350x300")
    ventana_gestor.configure(bg='#eae2b7')
    ventana_gestor.grab_set()
    ventana_gestor.title("Gestor de Empleados v1.0.0 BETA")
    ## LABEL PARA TODES
    Label(ventana_gestor, text="Menu principal", bg="#fcbf49", width="300", height="2").pack()
    Button(ventana_gestor, text="Agregar administrador", height="2", width="30", command = registrar_admin).pack()
    Button(ventana_gestor, text="Agregar empleados", height="2", width="30", command = agregar_empleados).pack()
    Button(ventana_gestor, text="Modificar empleado", height="2", width="30", command = modificar_empleados).pack()
    Button(ventana_gestor, text="Desactivar empleado", height="2", width="30", command = suspender_empleados).pack()

## Pantalla agregar admin    

def registrar_admin():
    global ventana_registrar_admin
    ventana_registrar_admin = Toplevel(ventana_gestor)
    ventana_registrar_admin.geometry("500x250")
    ventana_registrar_admin.configure(bg='#eae2b7')
    ventana_registrar_admin.grab_set()
    ventana_registrar_admin.title("Registrar administrador")
    global verifica_usuario_nuevo
    global verifica_clave_nuevo
 
    verifica_usuario_nuevo = StringVar()
    verifica_clave_nuevo = StringVar()
 
    global entrada_registro_usuario
    global entrada_registro_clave
 
    Label(ventana_registrar_admin, text="Introduzca nombre de usuario y contraseña para administrador nuevo", bg='#eae2b7').pack()
    Label(ventana_registrar_admin, text="Nombre usuario * ", bg='#eae2b7').pack()
    entrada_registro_usuario = Entry(ventana_registrar_admin, textvariable=verifica_usuario_nuevo)
    entrada_registro_usuario.pack()
    Label(ventana_registrar_admin, text="Contraseña * ", bg='#eae2b7').pack()
    entrada_registro_clave = Entry(ventana_registrar_admin, textvariable=verifica_clave_nuevo, show= '*')
    entrada_registro_clave.pack()
    Button(ventana_registrar_admin, text="Registrar", width=10, height=1, command = registrar).pack()

## funcion para registrar nuevo administrador

def registrar():
    print("registrado")

## pantalla modificar empleados

def modificar_empleados():
    global ventana_modificar_empleados
    ventana_modificar_empleados = Toplevel(ventana_gestor)
    ventana_modificar_empleados.geometry("500x350")
    ventana_modificar_empleados.configure(bg='#eae2b7')
    ventana_modificar_empleados.grab_set()
    ventana_modificar_empleados.title("Modificar empleado")
    
    Label(ventana_modificar_empleados, text="ID ", bg='#eae2b7').pack()
    entrada_id_empleado = Entry(ventana_modificar_empleados)
    entrada_id_empleado.pack()

    Label(ventana_modificar_empleados, text="Nombre ", bg='#eae2b7').pack()
    entrada_nombre_empleado = Entry(ventana_modificar_empleados)
    entrada_nombre_empleado.pack()

    Label(ventana_modificar_empleados, text="Apellido", bg='#eae2b7').pack()
    entrada_apellido_empleado = Entry(ventana_modificar_empleados)
    entrada_apellido_empleado.pack()

    Label(ventana_modificar_empleados, text="DNI", bg='#eae2b7').pack()
    entrada_dni_empleado = Entry(ventana_modificar_empleados)
    entrada_dni_empleado.pack()

    Label(ventana_modificar_empleados, text="Area", bg='#eae2b7').pack()
    entrada_area_empleado = Entry(ventana_modificar_empleados)
    entrada_area_empleado.pack()

    Button(ventana_modificar_empleados, text="Modificar empleado", height="2", width="30", command = modificar_empleado).pack()

## funcion para modificar empleado

def modificar_empleado():
    print("Empleado modificado")

# pantalla agregar empleados

def agregar_empleados():
    global ventana_agregar_empleados
    ventana_agregar_empleados = Toplevel(ventana_gestor)
    ventana_agregar_empleados.geometry("800x500")
    ventana_agregar_empleados.configure(bg='#eae2b7')
    ventana_agregar_empleados.grab_set()
    ventana_agregar_empleados.title("Agregar empleado")
        
    Label(ventana_agregar_empleados, text="Nombre ", bg='#eae2b7').pack()
    entrada_nombre_empleado = Entry(ventana_agregar_empleados)
    entrada_nombre_empleado.pack()

    Label(ventana_agregar_empleados, text="Apellido", bg='#eae2b7').pack()
    entrada_apellido_empleado = Entry(ventana_agregar_empleados)
    entrada_apellido_empleado.pack()

    Label(ventana_agregar_empleados, text="DNI", bg='#eae2b7').pack()
    entrada_dni_empleado = Entry(ventana_agregar_empleados)
    entrada_dni_empleado.pack()

    Label(ventana_agregar_empleados, text="Area", bg='#eae2b7').pack()
    entrada_area_empleado = Entry(ventana_agregar_empleados)
    entrada_area_empleado.pack()

    Button(ventana_agregar_empleados, text="Agregar empleado", height="2", width="30", command = agregar_empleado).pack()

    tv = ttk.Treeview(ventana_agregar_empleados)
    tv['columns']=('ID', 'Nombre', 'Apellido', 'DNI', 'Area')
    tv.column('#0', width=0, stretch=NO)
    tv.column('ID', anchor=CENTER, width=80)
    tv.column('Nombre', anchor=CENTER, width=80)
    tv.column('Apellido', anchor=CENTER, width=80)
    tv.column('DNI', anchor=CENTER, width=120)
    tv.column('Area', anchor=CENTER, width=120)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('ID', text='ID', anchor=CENTER)
    tv.heading('Nombre', text='Nombre', anchor=CENTER)
    tv.heading('Apellido', text='Apellido', anchor=CENTER)
    tv.heading('DNI', text='DNI', anchor=CENTER)
    tv.heading('Area', text='Area', anchor=CENTER)

    tv.insert(parent='', index=0, iid=0, text='', values=('45','Miguel','Rodriguez', '14243531', 'Operario de CNC')) # empleado hardcodeado para mostrar
    tv.pack()

## funcion para agregar empleados

def agregar_empleado():
    print("Empleado agregado")


def suspender_empleados():
    global ventana_suspender_empleados
    ventana_suspender_empleados = Toplevel(ventana_gestor)
    ventana_suspender_empleados.geometry("250x200")
    ventana_suspender_empleados.configure(bg='#eae2b7')
    ventana_suspender_empleados.grab_set()
    ventana_suspender_empleados.title("Suspender empleado")
    global id_usuario
 
    id_usuario = StringVar()
 
    global entrada_id_usuario
 
    Label(ventana_suspender_empleados, text="ID del empleado * ", bg='#eae2b7').pack()
    entrada_id_usuario = Entry(ventana_suspender_empleados, textvariable=id_usuario)
    entrada_id_usuario.pack()
    Button(ventana_suspender_empleados, text="Desactivar", width=10, height=1, command = desactivar).pack()

## funcion para desactivar empleado

def desactivar():
    print("desactivado")

app()