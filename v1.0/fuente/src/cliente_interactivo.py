import time
from busqueda_fuerza_bruta import busqueda_fuerza_bruta
from tabla_hash import construir_indice, busqueda_indexada

def cargar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='latin-1') as archivo:
        return archivo.readlines()

def realizar_busqueda_fuerza_bruta(texto, patron):
    inicio = time.perf_counter_ns()
    resultados = busqueda_fuerza_bruta(texto, patron)
    fin = time.perf_counter_ns()
    return resultados, (fin - inicio) / 1e9  # Convertir nanosegundos a segundos

def realizar_busqueda_indexada(indice, patron):
    inicio = time.perf_counter_ns()
    resultados = busqueda_indexada(indice, patron)
    fin = time.perf_counter_ns()
    return resultados, (fin - inicio) / 1e9  # Convertir nanosegundos a segundos

def main():
    texto = cargar_archivo('proyecto.tex')
    
    print("Construyendo índice...")
    indice = construir_indice(texto)
    
    while True:
        print("\nSeleccione el método de búsqueda:")
        print("1. Fuerza Bruta")
        print("2. Búsqueda Indexada")
        print("3. Salir")
        opcion = input("Opción: ")
        
        if opcion == '3':
            break
        
        patron = input("Ingrese el patrón o palabra a buscar: ")
        
        if opcion == '1':
            resultados, tiempo = realizar_busqueda_fuerza_bruta(texto, patron)
        elif opcion == '2':
            resultados, tiempo = realizar_busqueda_indexada(indice, patron)
        else:
            print("Opción no válida.")
            continue
        
        print(f"Tiempo de búsqueda: {tiempo:.6f} segundos")
        print(f"Resultados encontrados: {len(resultados)}")
        for resultado in resultados:
            print(f"Línea {resultado[0] + 1}: {resultado[1]}")

if __name__ == "__main__":
    main()
