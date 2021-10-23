from tkinter import *
import sqlite3
from tkinter import ttk

def app():
    global ventana_login
    ventana_login = Tk()
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()
    ventana_login.mainloop()

def verifica_login():
    if entrada_login_usuario.get() == "user" and entrada_login_clave.get() == "123":
        ingresar_pantalla_principal()
    else:
        print("nada que ver la psswrd")

def ingresar_pantalla_principal():
    global ventana_gestor
    ventana_gestor = Toplevel(ventana_login)
    ventana_gestor.geometry("300x250")
    ventana_gestor.title("Gestos de Empleados v1.0.0 BETA")
    pestas_color="DarkGrey"
    Label(ventana_gestor, text="Menu principal", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Button(ventana_gestor, text="Agregar administrador", height="2", width="30", bg=pestas_color).pack() #BOTÓN "Acceder"
    Button(ventana_gestor, text="Agregar empleado", height="2", width="30", bg=pestas_color).pack() #BOTÓN "Registrarse".
    Button(ventana_gestor, text="Desactivar empleado", height="2", width="30", bg=pestas_color).pack() #BOTÓN "Acceder"
    Button(ventana_gestor, text="Buscar empleado", height="2", width="30", bg=pestas_color).pack() #BOTÓN "Registrarse".
    

app()