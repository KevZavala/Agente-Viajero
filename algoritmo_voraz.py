from readData import readData
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

for idx,lista_costo in enumerate(matriz_total):
    fila_ciudad = { identificadores[idxf]: element for idxf, element in enumerate(lista_costo)}
    ciudad = Ciudad(identificadores[idx],fila_ciudad)
    diccionario_ciudades[identificadores[idx]] = ciudad

ciudades = Ciudades(diccionario_ciudades)

comienzo = time()
costos_de_caminos = { ciudades.camino_voraz(idx): ciudades.calcular_costo(ciudades.camino_voraz(idx)) for idx in identificadores[:20] }
camino_mas_corto = min(costos_de_caminos, key=costos_de_caminos.get)
costo = costos_de_caminos[camino_mas_corto]
final = time()
print('Tiempo: ', (final - comienzo))
print('Camino más corto: ', camino_mas_corto)
print('Traducción de camino:' , translate(camino_mas_corto))
print('Costo: ', costo)

