def construir_indice_con_diccionario(texto):
    indice = {}  # Diccionario para almacenar el índice
    
    for num_linea, linea in enumerate(texto, start=1):  # Iterar sobre cada línea en el texto
        palabras = linea.split()  # Obtener todas las palabras de la línea
        
        for palabra in palabras:  # Iterar sobre cada palabra en la línea
            palabra = palabra.strip().lower()  # Convertir a minúsculas y eliminar espacios
            
            if palabra:  # Verificar si la palabra no está vacía
                if palabra not in indice:  # Si la palabra no está en el índice, agregarla
                    indice[palabra] = set()  # Utilizamos un conjunto para evitar duplicados de líneas
                indice[palabra].add(num_linea)  # Agregar el número de línea al índice
    
    return indice  # Devolver el diccionario índice construido

