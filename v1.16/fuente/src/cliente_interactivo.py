import time
from tabla_hash import TablaHash
from busqueda_fuerza_bruta import busqueda_fuerza_bruta
from busqueda_con_diccionario import construir_indice_con_diccionario

# Función para cargar el contenido de un archivo de texto línea por línea
def cargar_archivo(nombre_archivo):
    # Determinar codificación según la extensión del archivo
    encoding = 'latin-1' if nombre_archivo.endswith('.tex') else 'utf-8'
    lineas = []
    # Abrir archivo y leer línea por línea
    with open(nombre_archivo, 'r', encoding=encoding) as archivo:
        for linea in archivo:
            lineas.append(linea)
    return lineas

# Función para realizar la búsqueda utilizando el método de fuerza bruta
def realizar_busqueda_fuerza_bruta(texto, patron):
    # Iniciar contador de tiempo
    inicio = time.perf_counter_ns()
    # Llamar a la función de búsqueda por fuerza bruta
    resultados = busqueda_fuerza_bruta(texto, patron)
    # Finalizar contador de tiempo y calcular duración de la búsqueda en microsegundos
    fin = time.perf_counter_ns()
    tiempo = (fin - inicio) / 1000  # Convertir nanosegundos a microsegundos
    # Preparar resultados numerados para mostrar
    resultados_numerados = []
    for resultado in resultados:
        resultados_numerados.append((resultado[0] + 1, resultado[1], resultado[2]))
    # Retornar resultados numerados y tiempo de búsqueda
    return resultados_numerados, tiempo

# Función para realizar la búsqueda utilizando el método indexado con TablaHash
def realizar_busqueda_indexada(tabla_hash, patron):
    # Iniciar contador de tiempo
    inicio = time.perf_counter_ns()
    # Buscar líneas en la TablaHash según el patrón
    lineas_encontradas = tabla_hash.buscar(patron)
    # Finalizar contador de tiempo y calcular duración de la búsqueda en microsegundos
    fin = time.perf_counter_ns()
    tiempo = (fin - inicio) / 1000  # Convertir nanosegundos a microsegundos
    # Inicializar lista para almacenar los resultados
    resultados = []
    
    # Para cada número de línea encontrado
    for num_linea in lineas_encontradas:
        # Obtener texto de la línea utilizando el índice base 1
        linea_texto = tabla_hash.texto[num_linea - 1]  # Restamos 1 porque num_linea es el índice base 1
        # Contar ocurrencias exactas del patrón en la línea (ignorando mayúsculas y minúsculas)
        contador = sum(1 for palabra in linea_texto.split() if palabra.lower() == patron.lower())
        # Agregar resultado (número de línea, contador, línea completa) a la lista de resultados
        resultados.append((num_linea, contador, linea_texto))
    # Retornar resultados y tiempo de búsqueda
    return resultados, tiempo

# Función para realizar la búsqueda utilizando el método con diccionario
def realizar_busqueda_con_diccionario(texto, patron):
    # Construir índice de palabras en el texto utilizando un diccionario
    indice = construir_indice_con_diccionario(texto)
    # Iniciar contador de tiempo
    inicio = time.perf_counter_ns()
    # Inicializar lista para almacenar los resultados
    resultados = []
    
    if patron in indice:
        lineas_encontradas = indice[patron]
    else:
        lineas_encontradas = set()
    
    for num_linea in lineas_encontradas:
        linea_texto = texto[num_linea - 1]  # Obtener texto de la línea utilizando el índice base 0
        contador = 0  # Inicializar contador de ocurrencias del patrón en la línea
        
        palabras = linea_texto.split()  # Dividir la línea en palabras
        
        for palabra in palabras:
            if palabra.strip().lower() == patron.lower():
                contador += 1
        
        if contador > 0:
            resultados.append((num_linea, linea_texto.strip(), contador))
    
    # Finalizar contador de tiempo y calcular duración de la búsqueda en microsegundos
    fin = time.perf_counter_ns()
    tiempo = (fin - inicio) / 1000  # Convertir nanosegundos a microsegundos
    # Retornar resultados y tiempo de búsqueda
    return resultados, tiempo



# Función principal que ejecuta el programa interactivo de búsqueda
def main():
    while True:
        # Mostrar menú para seleccionar archivo
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
        
        # Asignar nombre de archivo según la opción seleccionada
        if opcion_archivo == '1':
            nombre_archivo = 'proyecto.tex'
        elif opcion_archivo == '2':
            nombre_archivo = 'hawking-stephen-historia-del-tiempo.txt'
        elif opcion_archivo == '3':
            nombre_archivo = 'biblia.txt'
        
        # Cargar el contenido del archivo seleccionado como texto
        texto = cargar_archivo(nombre_archivo)
        # Inicializar la TablaHash con el texto del archivo seleccionado
        tabla_hash = TablaHash(texto)
        
        while True:
            # Mostrar menú para seleccionar método de búsqueda
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
            
            # Leer el patrón a buscar
            patron = input("Ingrese el patrón a buscar: ")
            
            # Realizar la búsqueda según la opción seleccionada
            if opcion_busqueda == '1':
                resultados, tiempo = realizar_busqueda_fuerza_bruta(texto, patron)
                print(f"Tiempo de búsqueda: {tiempo:.6f} microsegundos")
                print(f"Lineas encontradas: {len(resultados)}")
                print(f"Total de búsquedas encontradas: {sum(resultado[2] for resultado in resultados)} \n")
                for resultado in resultados:
                    print(f"Línea {resultado[0]} | (Apariciones: {resultado[2]}): {resultado[1]}")
            
            elif opcion_busqueda == '2':
                resultados, tiempo = realizar_busqueda_indexada(tabla_hash, patron)
                print(f"Tiempo de búsqueda: {tiempo:.6f} microsegundos")
                print(f"Lineas encontradas: {len(resultados)}")
                print(f"Total de búsquedas encontradas: {sum(resultado[1] for resultado in resultados)} \n")
                for resultado in resultados:
                    print(f"Línea {resultado[0]} | (Apariciones: {resultado[1]}): {resultado[2]}")
            
            elif opcion_busqueda == '3':
                resultados, tiempo = realizar_busqueda_con_diccionario(texto, patron)
                print(f"Tiempo de búsqueda: {tiempo:.6f} microsegundos")
                print(f"Lineas encontradas: {len(resultados)}")
                print(f"Total de búsquedas encontradas: {sum(resultado[2] for resultado in resultados)} \n")
                for resultado in resultados:
                    print(f"Línea {resultado[0]} | (Apariciones: {resultado[2]}): {resultado[1]}")

if __name__ == "__main__":
    main()
