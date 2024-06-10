import time
from busqueda_fuerza_bruta import busqueda_fuerza_bruta
from tabla_hash import TablaHash  
from busqueda_con_diccionario import construir_indice_con_diccionario

def cargar_archivo(nombre_archivo):
    encoding = 'latin-1' if nombre_archivo.endswith('.tex') else 'utf-8'
    with open(nombre_archivo, 'r', encoding=encoding) as archivo:
        return archivo.readlines()

def realizar_busqueda_fuerza_bruta(texto, patron):
    inicio = time.perf_counter_ns()
    resultados = busqueda_fuerza_bruta(texto, patron)
    fin = time.perf_counter_ns()
    tiempo = (fin - inicio) / 1000  # Microsegundos
    resultados_numerados = []
    for resultado in resultados:
        resultados_numerados.append((resultado[0] + 1, resultado[1], resultado[2]))
    return resultados_numerados, tiempo

def realizar_busqueda_indexada(texto, patron):
    indice = TablaHash(texto)  # Construir un nuevo índice cada vez
    inicio = time.perf_counter_ns()
    resultados = []
    lineas = indice.buscar(patron)  # Método buscar de TablaHash
    indice_linea = 1  # Contador de índice de línea
    for linea in lineas:
        contador = 0
        longitud_linea = len(linea)
        longitud_patron = len(patron)
        i = 0
        while i < longitud_linea:
            if linea[i:i+longitud_patron] == patron:
                contador += 1
                i += longitud_patron
            else:
                i += 1
        resultados.append((indice_linea, linea, contador))
        indice_linea += 1  # Incrementa el contador de índice de línea
    fin = time.perf_counter_ns()
    return resultados, (fin - inicio) / 1000  # Microsegundos

def realizar_busqueda_con_diccionario(texto, patron):
    indice = construir_indice_con_diccionario(texto)
    inicio = time.perf_counter_ns()
    resultados = []  # Inicializar lista de resultados
    num_linea = 1
    for linea in texto:
        palabra_actual = ''  # Inicializar la palabra actual
        contador = 0
        for caracter in linea:
            if caracter == ' ' or caracter == '\n':  # Si encontramos un espacio o un salto de línea, verificamos si la palabra actual es igual al patrón
                if palabra_actual == patron:
                    contador += 1
                palabra_actual = ''  # Reiniciar la palabra actual
            else:
                palabra_actual += caracter  # Agregar el caracter a la palabra actual
        if palabra_actual == patron:  # Verificar la última palabra de la línea
            contador += 1
        if contador > 0:  # Solo agregar resultados si hay al menos una ocurrencia
            resultados.append((num_linea, linea, contador))
        num_linea += 1
    fin = time.perf_counter_ns()
    tiempo = (fin - inicio) / 1000  # Microsegundos
    return resultados, tiempo

def main():
    while True:
        print("\nSeleccione el archivo a utilizar:")
        print("1. proyecto.tex")
        print("2. hawking-stephen-historia-del-tiempo.txt")
        print("3. biblia.txt")
        print("4. Salir")
        opcion_archivo = input("Opción: ")
        
        if opcion_archivo == '4':
            break
        elif opcion_archivo not in ['1', '2', '3']:
            print("Opción no válida.")
            continue
        
        if opcion_archivo == '1':
            nombre_archivo = 'proyecto.tex'
        elif opcion_archivo == '2':
            nombre_archivo = 'hawking-stephen-historia-del-tiempo.txt'
        elif opcion_archivo == '3':
            nombre_archivo = 'biblia.txt'
        
        texto = cargar_archivo(nombre_archivo)
        
        while True:
            print("\nSeleccione el método de búsqueda:")
            print("1. Fuerza Bruta")
            print("2. Búsqueda Indexada")
            print("3. Búsqueda con Diccionario")
            print("4. Cambiar archivo")
            print("5. Salir")
            opcion_busqueda = input("Opción: ")
            
            if opcion_busqueda == '5':
                return
            elif opcion_busqueda == '4':
                break
            elif opcion_busqueda not in ['1', '2', '3']:
                print("Opción no válida.")
                continue
            
            patron = input("Ingrese el patrón a buscar: ")
            
            if opcion_busqueda == '1':
                resultados, tiempo = realizar_busqueda_fuerza_bruta(texto, patron)
            elif opcion_busqueda == '2':
                resultados, tiempo = realizar_busqueda_indexada(texto, patron)
            elif opcion_busqueda == '3':
                 resultados, tiempo = realizar_busqueda_con_diccionario(texto, patron)
            
            lineas_encontradas = len(resultados)
            busquedas_encontradas = sum(resultado[2] for resultado in resultados)
            
            print(f"Tiempo de búsqueda: {tiempo:.6f} microsegundos")
            print(f"Lineas encontradas: {lineas_encontradas}")
            print(f"Total de búsquedas encontradas: {busquedas_encontradas} \n")
            for resultado in resultados:
                pass 
                #print(f"Línea {resultado[0]} | (Apariciones: {resultado[2]}): {resultado[1]}")

if __name__ == "__main__":
    main()