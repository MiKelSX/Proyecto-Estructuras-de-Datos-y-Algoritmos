class TablaHash:
    def __init__(self):
        self.tabla = {}
    
    def agregar(self, clave, valor):
        if clave not in self.tabla:
            self.tabla[clave] = []
        self.tabla[clave].append(valor)
    
    def buscar(self, clave):
        return self.tabla.get(clave, [])

def construir_indice(texto):
    indice = TablaHash()
    for i, linea in enumerate(texto):
        palabras = linea.split()
        for palabra in palabras:
            indice.agregar(palabra, (i, linea.strip()))
    return indice

def busqueda_indexada(indice, patron):
    return indice.buscar(patron)
