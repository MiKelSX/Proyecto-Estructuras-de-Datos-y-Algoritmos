def busqueda_fuerza_bruta(texto, patron):
    resultados = []  # Lista para almacenar los resultados encontrados
    indice_linea = 0  # Índice para recorrer las líneas del texto
    
    # Iterar sobre cada línea en el texto
    while indice_linea < len(texto):
        linea = texto[indice_linea]  # Obtener la línea actual
        contador = contar_patron(linea, patron)  # Contar las ocurrencias del patrón en la línea
        
        # Si se encontraron ocurrencias, agregar a los resultados
        if contador > 0:
            resultados.append((indice_linea, linea, contador))
        
        indice_linea += 1  # Pasar a la siguiente línea
    
    return resultados  # Devolver todos los resultados encontrados


def contar_patron(linea, patron):
    contador = 0  # Inicializar el contador de ocurrencias
    longitud_patron = len(patron)  # Obtener la longitud del patrón
    longitud_linea = len(linea)  # Obtener la longitud de la línea
    
    # Iterar sobre cada posible subcadena en la línea
    for i in range(longitud_linea - longitud_patron + 1):
        # Comparar la subcadena con el patrón y contar las ocurrencias
        if linea[i:i+longitud_patron] == patron:
            contador += 1  # Incrementar el contador si se encuentra una ocurrencia
            
    return contador  # Devolver el total de ocurrencias encontradas
