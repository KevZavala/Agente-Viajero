from readData import readData
from permutaciones2 import deter
from model import Ciudad
from model import Ciudades
from time import time
from translate import translate

matriz_ciudades = readData('data/ciudades_data_prueba.xlsx')
matriz_gasolina = readData('data/gasolina_data_prueba.xlsx')

identificadores = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
diccionario_identificadores = {i:f'C{idx}' for idx,i in enumerate(identificadores)}

diccionario_ciudades = {}

matriz_total = [ [matriz_ciudades[idxf][idxc] + matriz_gasolina[idxf][idxc] for idxc,celda in enumerate(matriz_ciudades)] for idxf, fila in enumerate(matriz_ciudades)]
print(matriz_total)

for idx,lista_costo in enumerate(matriz_total):
    fila_ciudad = { identificadores[idxf]: element for idxf, element in enumerate(lista_costo)}
    ciudad = Ciudad(identificadores[idx],fila_ciudad)
    diccionario_ciudades[identificadores[idx]] = ciudad

ciudades = Ciudades(diccionario_ciudades)

tamano_evaluacion = 14

comienzo = time()
permutaciones = deter(identificadores[:tamano_evaluacion])

ruta_seleccionada = next(permutaciones)
ruta_seleccionada_2 = ruta_seleccionada[0:-2] + ruta_seleccionada[:-3:-1]

ciudades.agregar_camino(ruta_seleccionada)
ciudades.evaluar_camino(ruta_seleccionada_2)


for permutacion in permutaciones:
    if permutacion[0] != 'A': break
    ciudades.evaluar_camino(permutacion)
    ciudades.evaluar_camino(permutacion[0:-2] + permutacion[:-3:-1])

final = time()


print('Camino más corto: ',ciudades.camino_corto)

print('Camino traducido: ', translate(ciudades.camino_corto))
print('Costo del camino: ',ciudades.costo_camino_corto)
print('Tiempo:', (final - comienzo))