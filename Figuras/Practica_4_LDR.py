import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_frame = 'datos_p4.xlsx'
data1 = pd.read_excel(data_frame)


datacalibracion = data1.Ccalibracion[0:5]
conductividad_calibracion = data1.Scalibracion[0:5]

area = 1.3951

E = data1.Concentracion/area

#Para la grafica de calibracion
plt.style.use('seaborn-darkgrid')
#plt.style.use('seaborn-pastel')
plt.figure('Curva_de_calibracion')
plt.plot(datacalibracion,conductividad_calibracion,':b')
#plt.text(0.025,1750,'Vamos a ver que pedo')
plt.title('Grafica de Calibracion')
plt.xlabel('Concentracion (M)')
plt.ylabel('Conductividad (mS)')
plt.grid(True)
plt.savefig('Curva_calibracion.pdf')

'''Fiura C'''
plt.figure('Curva_C')
plt.plot(data1.tiempo,data1.Concentracion,':b')
plt.title('Curva de equilibrio')
plt.ylabel('Concentracion[M]')
plt.xlabel('Tiempo[min]')
plt.grid(True)
plt.savefig('fig_concentracion.pdf')

'''Fiura E'''
plt.figure('Curva_E')
plt.plot(data1.tiempo,E,':b')
plt.title('Curva E')
plt.ylabel('E (1/min)')
plt.xlabel('Tiempo (min)')
plt.grid(True)
plt.savefig('fig_curva_E.pdf')

'''Fiura Et'''
Et = E*data1.tiempo

plt.figure('Curva_Et')
plt.axis([0,190,0,1.1])
plt.plot(data1.tiempo,Et,':b')
plt.title('Curva Et')
plt.ylabel('E (1/min)')
plt.xlabel('Tiempo (min)')
plt.grid(True)
plt.savefig('fig_Curva_Et.pdf')



