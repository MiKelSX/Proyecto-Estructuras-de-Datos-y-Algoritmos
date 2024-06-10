def busqueda_fuerza_bruta(texto, patron):
    resultados = []
    indice_linea = 0
    
    while indice_linea < len(texto):
        linea = texto[indice_linea]
        contador = contar_patron(linea, patron)
        if contador > 0:
            resultados.append((indice_linea, linea, contador))
        indice_linea += 1
        
    return resultados


def contar_patron(linea, patron):
    contador = 0
    longitud_patron = len(patron)
    longitud_linea = len(linea)
    
    for i in range(longitud_linea - longitud_patron + 1):
        if linea[i:i+longitud_patron] == patron:
            contador += 1
            
    return contador