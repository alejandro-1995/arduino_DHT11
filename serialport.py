
import asyncio
import threading
import time
from datetime import datetime, timedelta
import serial
import db

varcambio = 0

def leer_datos (varcambio):
    if (varcambio==1):
        ahora = datetime.now()
        ahorastring= str(ahora).format('YYYY-MM-DD-HH-MM.SS.SSS')
        list_values = []
        list_in_floats = []
        arduino = serial.Serial('COM8', 9600)
        arduino_data = arduino.readline()
        decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
        list_values = decoded_values.split('x')
        for item in list_values:
            list_in_floats.append(float(item))
        Temperatura = list_in_floats[0]
        Humedad = list_in_floats[1]
        arduino_data = 0
        list_in_floats.clear()
        list_values.clear()
        arduino.close()
        hilo = threading.Thread(target=db.insert_record, args=(ahorastring,Temperatura, Humedad))
        hilo.start()
        #db.insert_record(ahorastring,Temperatura, Humedad)
        #print (ahorastring, Temperatura, Humedad)
