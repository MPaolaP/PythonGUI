import tkinter as tk
from tkinter import messagebox

def enviar_saludo():
    nombre = entrada_nombre.get()
    messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")

def cambiar_color():
    colores = ["red", "blue", "green", "yellow", "orange", "purple"]
    color = colores[contador.get() % len(colores)]
    ventana.configure(bg=color)
    contador.set(contador.get() + 1)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Usuario")
ventana.geometry("300x200")

# Contador para cambiar el color
contador = tk.IntVar()
contador.set(0)

# Crear los widgets
etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_nombre.pack(pady=10)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_saludo)
boton_enviar.pack(pady=10)

boton_color = tk.Button(ventana, text="Cambiar color", command=cambiar_color)
boton_color.pack(pady=5)

# Iniciar el loop principal de la ventana
ventana.mainloop()