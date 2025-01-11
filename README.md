# Proyecto Estructuras de Datos y Algoritmos

<h3>Optimización de Búsqueda en Texto</h3>

Este repositorio contiene la implementación y evaluación de métodos eficientes de búsqueda en texto. El objetivo principal es determinar experimentalmente si la búsqueda indexada es más efectiva que otros métodos como la fuerza bruta o la búsqueda por diccionario, optimizando el tiempo de procesamiento y la gestión de grandes volúmenes de datos.

## 📋 Características

- **Comparación de Métodos de Búsqueda:**
  - Búsqueda por Fuerza Bruta.
  - Búsqueda Indexada utilizando Tablas de Hash.
  - Búsqueda por Diccionario.
- **Cliente Interactivo:** Interfaz para cargar textos, seleccionar métodos de búsqueda y visualizar resultados.
- **Pruebas Experimentales:** Evaluación de tiempos de búsqueda con diferentes archivos y patrones.

## 📑 Contenido del Proyecto

1. **Introducción:** Contexto y objetivos del proyecto.
2. **Análisis del Problema:** Condiciones, casos límite y metodología.
3. **Solución del Problema:**
   - Algoritmos implementados.
   - Construcción de índices hash y diccionarios.
   - Cliente interactivo para realizar pruebas.
4. **Discusión y Resultados:** Comparación de métodos según eficiencia y escenarios.
5. **Conclusión:** Principales hallazgos y posibles aplicaciones.
6. **Anexos:** Fuentes y referencias utilizadas.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje de Programación:** Python 3.13 o superior.
- **Estructuras de Datos:** Tablas de Hash y Diccionarios.

## 🚀 Funcionalidades

### Métodos de Búsqueda
- **Fuerza Bruta:** Busca coincidencias línea por línea.
- **Indexación con Tablas de Hash:** Almacena posiciones de palabras para búsquedas rápidas.
- **Diccionarios:** Mapea palabras únicas a las líneas donde aparecen.

### Cliente Interactivo
- Carga de archivos de texto.
- Selección de métodos de búsqueda.
- Visualización de resultados con tiempo de búsqueda y líneas encontradas.

### Archivos de Prueba
- **`proyecto.tex`**
- **`hawking-stephen-historia-del-tiempo.txt`**
- **`biblia.txt`**

## 📂 Estructura del Proyecto
├── fuente/ 
  
  │     -  -   ├─── EXECUTE
  
  │     -  -   ├── README
  
  │     -  -   ├── src/
  
  │     -  -   │     -  -   ├── cliente_interactivo.py
  
  │     -  -   │     -  -   ├── tabla_hash.py
  
  │     -  -   │     -  -   ├── busqueda_fuerza_bruta.py
  
  │     -  -   │     -  -   ├── busqueda_con_diccionario.py
  
  │     -  -   │     -  -   └── foo.bar
  
  ├── informe/
  
  │     -  -   ├── Cornejo_Gonzalez.pdf
  
  │     -  -   ├── Cornejo_Gonzalez.tex
  
  │     -  -   └── Cornejo_Gonzalez.zip
  
  ├── proyecto.tex
  
  ├── hawking-stephen-historia-del-tiempo.txt
  
  └── biblia.txt


## 👥 Autor

- Miguel Cornejo (Persona que hizo TODO el trabajo)

## 🗓️ Fecha de Entrega
13 de junio de 2024

## ⚠️ Advertencia y Licencia

Este proyecto ha sido desarrollado con fines educativos para ilustrar conceptos y técnicas en el diseño de bases de datos. **No se autoriza el uso directo de este material para implementaciones reales sin una evaluación técnica y contextual adecuada.**

### Términos de Uso
1. Los autores no se hacen responsables por el uso indebido, modificaciones o riesgos asociados derivados de este proyecto.
2. Este repositorio está disponible públicamente para promover el aprendizaje. Si se utiliza como base para otros trabajos, **se debe dar el debido crédito a al autor o autores originales citando este repositorio como referencia.**
3. Cualquier implementación que derive de este código o diseño debe cumplir con los estándares éticos y legales aplicables en el contexto de uso.

Se recomienda estudiar el código y adaptar cualquier implementación según las necesidades específicas, siempre evaluando su viabilidad y seguridad.
