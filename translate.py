

def translate( texto ):
    identificador = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    diccionario = { letra: idx + 1 for idx, letra in enumerate(identificador) }
    result = ''
    for letra in texto:
        result += f'C{diccionario[letra]}->'
    result += f'C{diccionario[texto[0]]}'
    return result

if __name__ == '__main__':
    print(translate('ARTQBNOIMLDJHCGPSEKF'))