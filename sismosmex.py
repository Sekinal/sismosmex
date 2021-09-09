import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit

sns.set_style("ticks")

sismos = pd.read_csv('sismos.csv', skiprows=4)
sismos = sismos.iloc[:-7]
enero = 0
febrero = 0
marzo = 0
abril = 0
mayo = 0
junio = 0
julio = 0
agosto = 0
septiembre = 0
octubre = 0
noviembre = 0
diciembre = 0
contador = 0
print(sismos)

for fecha in sismos['Fecha']:
    year, month, day = fecha.split('-')
    magnitud = sismos['Magnitud'][contador]
    if magnitud == 'no calculable':
        magnitud = 0
    else:
        magnitud = float(magnitud)
    if magnitud >= 1:
        if month == '01':
            enero += 1
        elif month == '02':
            febrero += 1
        elif month == '03':
            marzo += 1
        elif month == '04':
            abril += 1
        elif month == '05':
            mayo += 1
        elif month == '06':
            junio += 1
        elif month == '07':
            julio += 1
        elif month == '08':
            agosto += 1
        elif month == '09':
            septiembre += 1
        elif month == '10':
            octubre += 1
        elif month == '11':
            noviembre += 1
        elif month == '12':
            diciembre += 1
    contador += 1

meses = {
    'Enero': enero,
    'Febrero': febrero,
    'Marzo': marzo,
    'Abril': abril,
    'Mayo': mayo,
    'Junio': junio,
    'Julio': julio,
    'Agosto': agosto,
    'Septiembre': septiembre,
    'Octubre': octubre,
    'Noviembre': noviembre,
    'Diciembre': diciembre
}

keys = meses.keys()
valores = meses.values()

plt.title('Sismos de magnitud mayor o igual a 5 grados Richter. Datos del 2000 al 2021.')
plt.xlabel('Meses')
plt.ylabel('Número de sismos significativos.')
plt.bar(keys,valores, color='red')
plt.show()