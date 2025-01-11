def busqueda_fuerza_bruta(texto, patron):
    resultados = []
    for i, linea in enumerate(texto):
        if patron in linea:
            resultados.append((i, linea.strip()))
    return resultados
