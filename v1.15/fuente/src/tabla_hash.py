class TablaHash:
    def __init__(self, texto):
        self.tabla = {}
        self.vocabulario = {}
        self.contador_palabras = 0
        self.construir_indice(texto)

    def agregar(self, palabra, linea):
        if palabra not in self.vocabulario:
            self.vocabulario[palabra] = self.contador_palabras
            self.tabla[self.contador_palabras] = []
            self.contador_palabras += 1
        indice = self.vocabulario[palabra]
        self.tabla[indice].append(linea)

    def buscar(self, palabra):
        if palabra in self.vocabulario:
            indice = self.vocabulario[palabra]
            return self.tabla[indice]
        else:
            return []

    def busqueda_indexada(self, palabra):
        return self.buscar(palabra)

    def construir_indice(self, texto):
        # Primera pasada para construir el vocabulario
        for linea in texto:
            palabra_actual = ''
            for caracter in linea:
                if caracter == ' ' or caracter == '\n':
                    if palabra_actual:
                        self.agregar(palabra_actual, linea)
                        palabra_actual = ''
                else:
                    palabra_actual += caracter
            if palabra_actual:
                self.agregar(palabra_actual, linea)