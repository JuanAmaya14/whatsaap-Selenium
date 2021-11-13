import tkinter as tk
from tkinter import ttk

def enviar(name):
    _name = name.get()
    return _name

ventana = tk.Tk()
ventana.title("Principal")
ventana.geometry('380x300')
ventana.configure(background='black')

etiqueta1 = tk.Label(ventana,text = "Enviar mensaje", bg= "black", fg = "snow")
name = ttk.Entry(ventana)
aceptar = ttk.Button(ventana, text="Aceptar", command=enviar(name))
cancelar = ttk.Button(ventana,text="Cancelar")


name.place(x=50, y=50)

aceptar.place(x=150, y=100)
cancelar.place(x=60, y=100)

etiqueta1.pack(fill = tk.X)

ventana.mainloop() 