"""
Created on Sat Aug 27 18:20:13 2022
@author: Coqui
"""

import pandas as pd
import matplotlib.pyplot as plt

#archivo = "Ocupados_Genero.csv"
archivo = "https://cdn.produccion.gob.ar/cdn-mineria/Ocupados_Genero.csv"
datos = pd.read_csv(archivo, header=0, names=['Trimestre', 'Genero', 'Empleados'])
print(datos)

#Llenamos listas con valores a mujeres y hombres
totalFem = 0
mujeres = []
for element in range(0, len(datos['Empleados']), 3):
    mujeres.append(datos['Empleados'][element])
    totalFem = totalFem + int(datos['Empleados'][element])

totalMasc = 0 
hombres = []
for element in range(1, len(datos['Empleados']), 3):
    hombres.append(datos['Empleados'][element])
    totalMasc = totalMasc + int(datos['Empleados'][element])
    
print(f"Esto es femeninos: {mujeres}")
print(f"Esto es hombres: {hombres}")



#color y leyenda a cada curva
plt.plot(mujeres, label='Femenino')
plt.plot(hombres, label='Masculino')

plt.legend() #muestra los label

#nombres a los ejes
plt.ylabel('Empleados')
plt.xlabel('Trimestre')

plt.title('Empleados segun sexo')
plt.grid()

plt.show()


fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['Mujeres', 'Hombres']

ax.bar(categories, [totalFem, totalMasc]);





















