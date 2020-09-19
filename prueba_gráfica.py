import sqlite3
import pandas as pd 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time
from time import sleep




def hacer_grafica():
	miconexion = sqlite3.connect("MIBASE")
	micursor = miconexion.cursor()
	datos = pd.read_sql_query("SELECT * FROM REGISTROS", miconexion)
	df=pd.DataFrame(datos)
	miplot = df.plot()
	plt.title('Gráfica de Temperatura y Humedad')
	plt.xlabel('Observación')
	plt.ylabel('Lectura')
	plt.show()
	miconexion.close()




