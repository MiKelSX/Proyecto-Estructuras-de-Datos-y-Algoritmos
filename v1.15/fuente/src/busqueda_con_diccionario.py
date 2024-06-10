def construir_indice_con_diccionario(texto):
    indice = {}
    num_linea = 0
    for linea in texto:
        palabra_actual = ''
        for caracter in linea:
            if caracter == ' ' or caracter == '\n':
                if palabra_actual:
                    if palabra_actual not in indice:
                        indice[palabra_actual] = []
                    indice[palabra_actual].append(num_linea + 1)
                    palabra_actual = ''
            else:
                palabra_actual += caracter
        if palabra_actual:
            if palabra_actual not in indice:
                indice[palabra_actual] = []
            indice[palabra_actual].append(num_linea + 1)
        num_linea += 1
    return indice

def buscar_con_diccionario(indice, palabra):
    if palabra in indice:
        return indice[palabra]
    else:
        return []