from tkinter import *
from tkinter import messagebox
import serialport
import threading
import prueba_gráfica
import db

def crearbase():
	db.crear()

def leer():
	serialport.varcambio=1
	thread = threading.Thread(target=serialport.leer_datos, args=(1, ))
	thread.start()
	miraiz.after(10000, escanear)

def escanear():
	mivariable=serialport.varcambio
	if (mivariable==1):
		leer()
		
def on_closing():
    if messagebox.askokcancel("Cerrar","¿Realmente deseas cerrar?"):
         miraiz.destroy()
        

def detener():
	serialport.varcambio=0

def graficar():
		prueba_gráfica.hacer_grafica()


miraiz=Tk()

miraiz.title("Youtube: Alejandro Hernández---Interfaz de Usuario")

miframe = Frame(miraiz)
miframe.pack()

botonleer= Button(miframe, text="LEER DATOS", command=leer)
botonleer.grid(row=0, column=0, sticky="e", padx=10, pady=10)


botondejar= Button(miframe, text="DEJAR DE LEER DATOS",command=detener)
botondejar.grid(row=0, column=1, sticky="e", padx=10, pady=10)


botongrafico=Button(miframe, text="VER GRÁFICO", command=graficar)
botongrafico.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botoncrearbase=Button(miframe, text="CREAR BASE", command=crearbase)
botoncrearbase.grid(row=1, column=1, sticky="e", padx=10, pady=10)


miraiz.protocol("WM_DELETE_WINDOW", on_closing)
miraiz.mainloop()
