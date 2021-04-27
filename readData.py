import pandas

def readData(file):
    matriz_data = pandas.read_excel(file, header=None)
    return matriz_data.values.tolist()

if __name__ == '__main__':

    #DataFiles
    ciudades_data = 'data/ciudades_data.xlsx'
    gasolina_data = 'data/gasolina_data.xlsx'

    # call method from read DataFiles
    data = readData(ciudades_data)
    print(data)