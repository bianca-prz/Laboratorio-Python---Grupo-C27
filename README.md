# 𝑳𝒂𝒃𝒐𝒓𝒂𝒕𝒐𝒓𝒊𝒐 𝑷𝒉𝒚𝒕𝒐𝒏 - 𝑮𝒓𝒖𝒑𝒐 𝑪𝟐𝟕
## 👥 Integrantes
* **Araujo Ledezma, Pilar** - Legajo: 31527
* **Perez, Bianca Belen** - Legajo: 31883
* **Sosa, Milena Tali** - Legajo:  31041

## 📚 Información Académica

**Universidad Tecnológica Nacional - Facultad Regional Resistencia**

<p align="center">
  <img width="222" height="227" alt="log-UTN 2" src="https://github.com/user-attachments/assets/4e1f2f7f-0178-444f-911a-454a80a7fc89" />
</p>

* **Cátedra:** Algoritmos y Estructuras de Datos.
* **Comisión:** C
* **Año:** 2026
  
## 📑 Descripción General del Sistema
Este sistema es una herramienta interactiva por consola diseñada para administrar el proceso de inscripción de estudiantes a diferentes ofertas académicas. El software implementa de manera eficiente las reglas de negocio de una academia utilizando persistencia de datos en archivos planos de texto (`.txt`).

### Características Principales:
* **Modularización Avanzada:** Estructurado completamente mediante funciones y procedimientos especializados, lo que facilita el mantenimiento y la escalabilidad del código.
* **Persistencia de Datos Seguro:** Control de lectura y escritura de archivos (`cursos.txt`, `inscripciones.txt`, `espera.txt`) con manejo preventivo de errores de permisos (`PermissionError`) o archivos ausentes.
* **Optimización de Búsqueda:** Utiliza la estructura de datos `Counter` de la librería `collections` para procesar el conteo de alumnos inscriptos en tiempo lineal realizando una única lectura.
* **Validaciones Robustas:** * Filtrado estricto de nombres (no se permiten campos vacíos, números ni caracteres especiales).
    * Control de redundancia (evita que un mismo estudiante se inscriba dos veces al mismo curso mediante normalización con `.casefold()`).
    * Asignación automática a **Lista de Espera** cuando el cupo real del curso llega a cero.

### Arquitectura de Datos (Estructura de Archivos)
El sistema gestiona de forma autónoma tres secuencias de almacenamiento:

1.  **`cursos.txt`**: Catálogo general de la oferta académica. Almacena en líneas alternas el nombre del curso y su cupo máximo original (Inicializado por defecto con 6 cursos y cupo de 10).
2.  **`inscripciones.txt`**: Registro de alumnos efectivamente confirmados. Guarda pares de líneas de tipo `[Nombre Alumno]` y `[Curso]`.
3.  **`espera.txt`**: Registro secundario de desborde. Guarda de forma idéntica a las inscripciones a los alumnos que solicitaron un curso cuyo cupo ya estaba completo.

## ✅️ Instrucciones de Ejecución

### Requisitos Previos
* Tener instalado **Python 3.8** o superior en el sistema.
* Se recomiendan extensiones de python en el editor de código que disponga, permitiendo correr el código y corregirlo con mayor facilidad de ser necesario (como **Code Runner**, **Python** y **Pylance**)

### Pasos para Ejecutar el Programa

1.  **Clonar o Descargar el Proyecto:** Asegurate de tener el archivo principal de código fuente (por ejemplo, `sistema_inscripciones.py`) en una carpeta local de tu computadora.
2.  **Abrir una Terminal:** Navegá con la consola de comandos (`cmd`, `PowerShell` o terminal de Linux/macOS) hasta el directorio donde guardaste el archivo.
3.  **Interacción:** El programa creará automáticamente el catálogo inicial (`cursos.txt`) si no existiera previamente, y desplegará el menú interactivo con las opciones de visualización, registro de estudiantes y estadísticas. Para finalizar las operaciones de manera segura, seleccioná la opción `4` o escribí `salir`.
4. **Pruebas y Reinicio del Sistema:** Para realizar pruebas limpias o restablecer el sistema a su estado inicial de fábrica:
    - Cierre el programa desde el menú principal (Opción 4).
    - Borre manualmente los archivos generados en la misma carpeta: `cursos.txt`, `inscripciones.txt` y `espera.txt`.
    - Vuelva a iniciar el programa. El sistema detectará la ausencia de los archivos y creará automáticamente un catálogo limpio con los cupos iniciales en 10.

## 🗂 Metodología de trabajo y Uso de Inteligencia Artificial 
Para la organización y desarrollo de este taller, adoptamos un método de trabajo donde dividimos las tareas para optimizar los tiempos disponible antes de la fecha límite de entrega del proyecto, permitiendonos equilibrar la carga horaria y la complejidad del taller con el resto de nuestras responsabilidades académicas y personales.
 En primera instancia, optamos por diseñar una estructura básica del código, desarrollando el proceso y las funciones o procedimientos principales del algoritmo, utilizando el Pseudocódigo dictado por la cátedra. Implementamos **Inteligencia Artificial** como herramienta de asistencia para traducir nuestra lógica base al lenguaje Python. Utilizando el material teórico brindado por la cátedra, pudimos verificar la correlación directa y la equivalencia entre las estructuras de control en pseudocódigo y su sintaxis correspondiente en Python. Y, por último, mediante el diseño de prompts específicos y detallados, solicitamos a la IA la detección de posibles errores de lógica, y la propuesta de optimización y ámpliación del código.

### _Nuestro Desarrollo del Algoritmo En Pseudocódigo_

Acción SistemadeInscripciones es
  PROCEDIMIENTO 1: MOSTRAR CURSOS
   
    PROCEDIMIENTO mostrar_cursos()
        Curso: caracter
        Cupo: caracter
        
        Escribir ("LISTA DE CURSOS DISPONIBLES")
                ABRIR E/(cursos.txt)
        
        MIENTRAS NFDA (cursos.txt) HACER
            // Leemos el nombre del curso
            Leer (cursos.txt, curso)
            // Leemos el cupo que está en la siguiente línea
            Leer (cursos.txt, cupo)
            
            SI curso <> " " ENTONCES
                ESCRIBIR (“- ", curso, ". Cupos disponibles:", cupo)
            FIN_SI
        FIN_MIENTRAS
        
        CERRAR(cursos.txt)
    FIN_PROCEDIMIENTO


  FUNCION 2: Buscar Cupo
   
     FUNCION obtener_cupo_maximo(curso_buscado : Caracter) : Entero
      Curso_actual: Caracter
      Cupo_actual_str: Caracter
      Encontrado: Booleano // bandera de control
    
      obtener_cupo_maximo := 0
      Encontrado := Falso 
    
      ABRIR E/(cursos.txt)
    
      Mientras NFDA (cursos.txt) Y (Encontrado = Falso) hacer
        LEER(cursos.txt, curso_actual)
        LEER(cursos.txt, cupo_actual_str)
        
        SI curso_actual = curso_buscado ENTONCES
            obtener_cupo_maximo := CONVERTIR_A_ENTERO(cupo_actual_str)
            Encontrado := Verdadero // ¡Lo encontramos! Esto frena el bucle en la próxima vuelta
        FIN_SI
     FIN_MIENTRAS
    
     CERRAR(cursos.txt)
    FIN_FUNCION


PROCEDIMIENTO 3: REGISTRAR ALUMNO
    
    PROCEDIMIENTO registrar_inscripcion(alumno : caracter, curso : caracter)
        // Abrimos el archivo 
               ABRIR E/(inscripciones.txt) 
        
        // Guardamos los datos
        Escribir(inscripciones.txt, alumno)
        Escribir(inscripciones.txt, curso)
        
        CERRAR(inscripciones.txt)
        ESCRIBIR ("Estudiante registrado con éxito.")
    FIN_PROCEDIMIENTO



PROCEDIMIENTO 4: ESTADÍSTICAS POR CARRERA

     PROCEDIMIENTO mostrar_estadisticas()
       curso_catalogo : Caracter
       cupo_catalogo : Caracter
       alumno_inscripto : Caracter
       curso_inscripto : Caracter
       contador_por_curso : Entero
    
      ESCRIBIR ("ESTADÍSTICAS DE INSCRITOS POR CARRERA")
    
    // 1. Abrimos el archivo de cursos para saber qué carreras existen
    ABRIR E/(cursos.txt)
    
     MIENTRAS NO NFDA (cursos.txt) HACER
        LEER(cursos.txt, curso_catalogo)
        LEER(cursos.txt, cupo_catalogo)
        
        SI curso_catalogo <> " " ENTONCES
            // Cada vez que cambiamos de curso, el contador vuelve a 0
            contador_por_curso := 0
            
            // 2. Abrimos el archivo de inscripciones para contar los alumnos de este curso
            ABRIR(inscripciones.txt, LEER)
            
            MIENTRAS NO NFDA(inscripciones.txt) HACER
                LEER(inscripciones.txt, alumno_inscripto)
                LEER(inscripciones.txt, curso_inscripto)
                
                // Si el curso del alumno coincide con el curso que estoy analizando, sumo 1
                SI curso_inscripto = curso_catalogo ENTONCES
                    contador_por_curso := contador_por_curso + 1
                FIN_SI
            FIN_MIENTRAS
            
            // Cerramos inscripciones para que en la próxima vuelta se pueda leer desde el principio
            CERRAR(inscripciones.txt)
            
            // Mostramos el resultado en pantalla para esta carrera
            ESCRIBIR ("- ", curso_catalogo, ": ", contador_por_curso, " inscriptos.")
        FIN_SI
     FIN_MIENTRAS
    
     CERRAR("cursos.txt")
     FIN_PROCEDIMIENTO

PROCESO PRINCIPAL 
 
    PROCEDIMIENTO iniciar_programa()
        nombre_alumno : Caracter
        curso_elegido : Caracter
        cupo_disponible : Entero
        
        ESCRIBIR ("BIENVENIDOS")
        mostrar_cursos() // Muestra la lista
        
        ESCRIBIR "Ingrese Nombre y Apellido del alumno:"
        LEER (nombre_alumno)
        
        ESCRIBIR ("Ingrese el nombre del curso de manera exacta:")
        LEER (curso_elegido)
        
        // Buscamos el cupo
        cupo_disponible := obtener_cupo_maximo(curso_elegido)
        
              SI cupo_disponible > 0 ENTONCES
                  registrar_inscripcion(nombre_alumno, curso_elegido)
             sino
                  ESCRIBIR "El curso ingresado no existe."
        FIN_SI
        
        mostrar_estadisticas()
    FIN_ACCION

### _Prompt enviado a la IA (Claude):_

<p align="center">
<img width="1366" height="639" alt="image" src="https://github.com/user-attachments/assets/d3bd2dc0-6461-4706-ba4f-946fbe29ee0c" />
</p>

De la respuesta a este Prompt, obtenemos nuestro primer commit ("Traducción del código a Python"). Donde se corrigen errores de nuestro código base y se lo pasa a su versión del lenguaje solicitado.
Es por esto que, si bien este commit contiene todo nuestro desarrollo, debemos aclarar que **dicha estructura en pseudocódigo sí fue desarrollada en un lapso de tiempo más prolongado.**

Luego de esto realizamos ajustes para prevenir errores (como `try/except`) y cambiamos algunas funciones para lograr una mejora del sistema. Se agregaron por ejemplo:
`def obtener_todas_las_inscripciones` , `def obtener_cupo_máximo` , `def alumno_ya_inscripto` , `def validar_nombre` , `def inscribir_estudiante_flujo`. En consecuencia, se modifico el Proceso Principal, dejandolo mucho más limpio y legible, logrando un menu interactivo; quien se encarga de llamar a cada función según la opción elegida por el usuario. 
  - Cada uno de estos cambios fue comentado.


