import sqlite3
from tkinter import *
from tkinter import messagebox

def insert_record(fecha, TEMP, HUM):
    miconexion=sqlite3.connect("MIBASE")
    micursor = miconexion.cursor()
    micursor.execute ("INSERT INTO REGISTROS (FECHA, TEMPERATURA, HUMEDAD) VALUES (?, ?, ?)",(fecha,TEMP,HUM))
    miconexion.commit()
    w = str(fecha)
    h =str(w)[0:17]
    messagebox.showinfo("BBDD", "Registro agregado con éxito "+ "Fecha: " + str(h) + " " + "Temperatura: " + str(TEMP) + " "+ "°C" + " "+ "Humedad: " + str(HUM)+ " " + "%" )
    miconexion.close()


def crear():
    miconexion=sqlite3.connect("MIBASE")
    micursor = miconexion.cursor()
    try:
    	micursor.execute ("CREATE TABLE REGISTROS (FECHA VARCHAR(50), TEMPERATURA DECIMAL, HUMEDAD DECIMAL)")
    	messagebox.showinfo("BBDD", "Base de Datos creada con éxito")
    	miconexion.close()
    except:
    	messagebox.showwarning("¡Atención!", "La Base de Datos ya existe")

