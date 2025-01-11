class TablaHash:
    def __init__(self, texto):
        self.vocabulario = {}  # Diccionario para mapear palabras a índices
        self.construir_indice(texto)  # Construir el índice al inicializar la clase
    
    def construir_indice(self, texto):
        self.tabla = {}  # Diccionario para almacenar listas de líneas por índice
        self.texto = texto  # Guardar el texto completo como atributo de la instancia
        self.contador_palabras = 0  # Contador para asignar índices a palabras únicas
        num_linea = 1
        
        # Iterar sobre cada línea del texto
        for linea in texto:
            palabras = self.extraer_palabras(linea)  # Obtener lista de palabras en la línea
            for palabra in palabras:
                self.agregar(palabra, num_linea)  # Agregar palabra al índice
            num_linea += 1
    
    def agregar(self, palabra, num_linea):
        if palabra not in self.vocabulario:  # Si la palabra no está en el vocabulario
            self.vocabulario[palabra] = self.contador_palabras  # Asignar un nuevo índice a la palabra
            self.tabla[self.contador_palabras] = []  # Inicializar una lista vacía para las líneas
            self.contador_palabras += 1  # Incrementar el contador de índices
        
        indice = self.vocabulario[palabra]  # Obtener el índice de la palabra
        if num_linea not in self.tabla[indice]:  # Si la línea no está en la lista del índice
            self.tabla[indice].append(num_linea)  # Agregar la línea al índice
    
    def buscar(self, palabra):
        if palabra in self.vocabulario:  # Si la palabra está en el vocabulario
            indice = self.vocabulario[palabra]  # Obtener el índice asociado a la palabra
            return self.tabla[indice]  # Devolver la lista de líneas asociadas al índice
        else:
            return []  # Devolver una lista vacía si la palabra no está en el vocabulario
    
    def extraer_palabras(self, linea):
        palabra_actual = ''  # Variable para almacenar la palabra actual durante la iteración
        palabras = []  # Lista para almacenar todas las palabras encontradas en la línea
        
        # Iterar sobre cada caracter en la línea
        for caracter in linea:
            if caracter == ' ' or caracter == '\n':  # Si el caracter es un espacio o salto de línea
                if palabra_actual:  # Si hay una palabra almacenada en palabra_actual
                    palabras.append(palabra_actual)  # Agregar la palabra a la lista de palabras
                    palabra_actual = ''  # Reiniciar palabra_actual para la próxima palabra
            else:
                palabra_actual += caracter  # Construir la palabra agregando caracteres
        
        if palabra_actual:  # Para asegurar que la última palabra de la línea se agregue
            palabras.append(palabra_actual)
        
        return palabras  # Devolver la lista de palabras encontradas en la línea

