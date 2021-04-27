from copy import copy


class Ciudad:
    
    def __init__(self, identificador, fila):
        self.identificador = identificador
        self.fila = fila
    def __add__(self, ciudad):
        return self.fila[ciudad.identificador]

    def __str__(self):
        return f'Ciudad {self.identificador} - {self.fila}'

class Ciudades:
    
    camino_corto = ''
    costo_camino_corto = 0
    def __init__(self, diccionario_ciudades):
        self.ciudades = diccionario_ciudades
    
    def agregar_camino(self,cadena):
        self.camino_corto = cadena
        self.costo_camino_corto = self.calcular_costo(cadena)
    
    def evaluar_camino(self, cadena):
        costo = self.calcular_costo(cadena)
        if self.costo_camino_corto > costo:
            self.camino_corto = cadena
            self.costo_camino_corto = costo


    def calcular_costo(self, cadena):
        cadena += cadena[0]
        suma = 0
        ciudad_actual = self.ciudades[cadena[0]]
        for ciudad in cadena[1:]:
            suma += ciudad_actual + self.ciudades[ciudad]
            ciudad_actual = self.ciudades[ciudad]
        return suma
    
    def camino_voraz(self, ubicacion='A'):
        resultado = ubicacion
        while len(resultado) != len(self.ciudades):
            ciudad_ahora = copy(self.ciudades[ubicacion].fila)
            for letra in resultado:
                ciudad_ahora.pop(letra)
            camino_minimo = min(ciudad_ahora, key=ciudad_ahora.get)
            resultado += camino_minimo
            ubicacion = camino_minimo
        return resultado    


if __name__ == '__main__':
    from permutaciones import deter
    from time import time

    c1 = Ciudad('A',{'A':0, 'B':3, 'C': 4, 'D':2})
    c2 = Ciudad('B',{'A':3, 'B':0, 'C': 1, 'D':5})
    c3 = Ciudad('C',{'A':4, 'B':1, 'C': 0, 'D':2})
    c4 = Ciudad('D',{'A':2, 'B':5, 'C': 2, 'D':0})


    diccionario_ciudades = { 'A': c1, 'B': c2, 'C': c3, 'D': c4 }

    ciudades = Ciudades(diccionario_ciudades)

    cadenas = deter('ABCD')
    menor_costo = 0
    ruta_menor_costo = ''
    comienzo = time()
    for cadena in cadenas:
        costo = ciudades.calcular_costo(cadena)
        if costo < menor_costo or menor_costo == 0:
            menor_costo = costo
            ruta_menor_costo = cadena
    termino = time()
    print('Ruta con menor costo:', '-'.join(ruta_menor_costo) + '-' + ruta_menor_costo[0])
    print('Costo de la ruta:', menor_costo)
    print('Tiempo de calculo:', (termino - comienzo))