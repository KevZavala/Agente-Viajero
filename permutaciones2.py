from time import time


def deter(texto):
    if len(texto) == 2: yield texto
    else:
        for idx, element in enumerate(texto):
            menor = texto[0:idx] + texto[idx + 1:]
            permutaciones = deter(menor)
            for permutacion in permutaciones:
                yield element + permutacion



a = deter('ABCDE')



if __name__ == "__main__":

    comienzo = time()

    resultados = []
    for i in a:
        # resultados += 1
        resultados.append(len(set(i)))
        resultados.append(len(set(i[0:-2] + i[:-3:-1])))

    termino = time()
    print(resultados)
    print(len(set(resultados)))

    print('Tiempo: ',(termino - comienzo))
