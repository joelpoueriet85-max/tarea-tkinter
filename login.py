import os
import tkinter as tk
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

# Función 1: Capturar credenciales desde los campos de entrada
def capturar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    return usuario, contrasena

# Función 2: Validar las credenciales contra las variables de entorno
def validar_credenciales(usuario, contrasena):
    user_env = os.getenv("APP_USER")
    pass_env = os.getenv("APP_PASSWORD")
    return usuario == user_env and contrasena == pass_env

# Función 3: Mostrar el mensaje y cambiar el color en la interfaz
def mostrar_mensaje():
    usuario, contrasena = capturar_credenciales()
    
    if validar_credenciales(usuario, contrasena):
        label_mensaje.config(text="Acceso correcto", fg="green")
    else:
        label_mensaje.config(text="Usuario o contraseña incorrectos", fg="red")

# --- Configuración de la ventana principal ---
ventana = tk.Tk()
ventana.title("Validación de Credenciales")
ventana.geometry("320x230")
ventana.resizable(False, False)

# Campo Usuario
tk.Label(ventana, text="Usuario:", font=("Arial", 10)).pack(pady=(15, 5))
entry_usuario = tk.Entry(ventana, font=("Arial", 10))
entry_usuario.pack()

# Campo Contraseña (show="*" oculta los caracteres)
tk.Label(ventana, text="Contraseña:", font=("Arial", 10)).pack(pady=(10, 5))
entry_contrasena = tk.Entry(ventana, show="*", font=("Arial", 10))
entry_contrasena.pack()

# Botón de acción
btn_ingresar = tk.Button(
    ventana, 
    text="Iniciar Sesión", 
    command=mostrar_mensaje,
    font=("Arial", 10, "bold")
)
btn_ingresar.pack(pady=15)

# Etiqueta dinámica para el resultado
label_mensaje = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
label_mensaje.pack()

# Ejecutar la aplicación
ventana.mainloop()
