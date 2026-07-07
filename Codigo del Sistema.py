"""
Sistema de Gestión de Inscripciones - Academia
Traducción a Python del pseudocódigo original.
"""
from collection import Counter # cambio: se importó counter para leer el archivo de inscripciones de una sola vez (optimización) 
import os

ARCHIVO_CURSOS = "cursos.txt"
ARCHIVO_INSCRIPCIONES = "inscripciones.txt"
ARCHIVO_ESPERA = "espera.txt"

CUPO_INICIAL = 10
CURSOS_INICIALES = [
    "Programacion",
    "Diseno Grafico",
    "Marketing Digital",
    "Contabilidad",
    "Ingles",
    "Redes y Soporte Tecnico"
]


def inicializar_cursos():
    """Crea cursos.txt con los 6 cursos y cupo=10 SOLO si el archivo no existe aun.
    (El pseudocodigo original nunca creaba este archivo, asumia que ya existia)."""
    if not os.path.exists(ARCHIVO_CURSOS):
        try: #cambio: se agrega un try para manejar errores de escritura en el archivo 
        with open(ARCHIVO_CURSOS, "w", encoding="utf-8") as archivo:
            for curso in CURSOS_INICIALES:
                archivo.write(curso + "\n")
                archivo.write(str(CUPO_INICIAL) + "\n")
        except PermissionError: #cambio: se agrega un except para manejar errores de permisos de escritura en el archivo 
        print("Error de permisos al crear el catálogo de cursos. Asegurese de tener permisos de escritura en el directorio.")

def mostrar_cursos():
    """PROCEDIMIENTO 1: Muestra la lista de cursos disponibles con su cupo maximo."""
    print("\nLISTA DE CURSOS DISPONIBLES")
    lineas = leer_archivo_seguro(ARCHIVO_CURSOS)  # Cambio: Usa lectura segura -> Evita fallos si el archivo no existe o está bloqueado

    # cambio: Se usó zip(): Recorre de a pares de forma limpia y moderna sin usar índices manuales i e i+1 (Evita IndexError)
    for curso, cupo in zip(lineas[0::2], lineas[1::2]):
        print(f"- {curso}. Cupos disponibles: {cupo}")
    

def obtener_cupo_maximo(curso_buscado):
    """FUNCION 2: Devuelve el cupo MAXIMO original de un curso (segun cursos.txt).
    Devuelve 0 si el curso no existe en el catalogo."""
    lineas = leer_archivo_seguro(ARCHIVO_CURSOS) # CAMBIO: Se usa la función de lectura segura para evitar errores si el archivo no existe o está bloqueado 
    # CAMBIO: Se usó zip(): Recorre el catálogo de forma segura emparejando Curso y Cupo
    for curso_actual, cupo_actual_str in zip(lineas[0::2], lineas[1::2]):
        # CAMBIO: .casefold(): Compara ignorando mayúsculas/minúsculas ("Programacion" == "programacion")
        if curso_actual.casefold() == curso_buscado.casefold():
            try:
                return int(cupo_actual_str)  # CAMBIO: try/except -> Evita ValueError si el archivo fue editado con texto en vez de número
            except ValueError:
                return 0
    return 0


def contar_inscriptos(curso_buscado):
    """NUEVA FUNCION (no estaba en el pseudocodigo original).
    Cuenta cuantos alumnos ya estan inscriptos en un curso, leyendo inscripciones.txt.
    Es necesaria porque cursos.txt solo guarda el cupo MAXIMO inicial y nunca se actualiza,
    entonces sin esto no hay forma de saber cuantos lugares quedan realmente."""
    if not os.path.exists(ARCHIVO_INSCRIPCIONES):
        return 0  # si el archivo todavia no existe, nadie esta inscripto

    with open(ARCHIVO_INSCRIPCIONES, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    contador = 0
    for i in range(0, len(lineas), 2):
        curso_inscripto = lineas[i + 1].strip()
        if curso_inscripto == curso_buscado:
            contador += 1

    return contador


def registrar_inscripcion(alumno, curso):
    """PROCEDIMIENTO 3: Guarda al alumno en inscripciones.txt.
    Usamos modo "a" (append = agregar) para sumar al final del archivo
    sin borrar a los alumnos que ya estaban registrados."""
    with open(ARCHIVO_INSCRIPCIONES, "a", encoding="utf-8") as archivo:
        archivo.write(alumno + "\n")
        archivo.write(curso + "\n")

    print("Estudiante registrado con exito.")


def registrar_espera(alumno, curso):
    """NUEVO PROCEDIMIENTO (faltaba por completo en el pseudocodigo original).
    Guarda al alumno en espera.txt cuando el curso elegido ya no tiene cupos."""
    with open(ARCHIVO_ESPERA, "a", encoding="utf-8") as archivo:
        archivo.write(alumno + "\n")
        archivo.write(curso + "\n")

    print("El curso esta completo. El alumno fue agregado a la lista de espera.")


def mostrar_estadisticas():
    """PROCEDIMIENTO 4: Muestra cuantos alumnos estan inscriptos en cada curso."""
    print("\nESTADISTICAS DE INSCRITOS POR CARRERA")

    with open(ARCHIVO_CURSOS, "r", encoding="utf-8") as archivo:
        lineas_cursos = archivo.readlines()

    for i in range(0, len(lineas_cursos), 2):
        curso_catalogo = lineas_cursos[i].strip()
        if curso_catalogo != "":
            contador_por_curso = contar_inscriptos(curso_catalogo)
            print(f"- {curso_catalogo}: {contador_por_curso} inscriptos.")


def iniciar_programa():
    """PROCESO PRINCIPAL: controla el flujo. Se agrego un bucle WHILE para poder
    inscribir a VARIOS alumnos (el pseudocodigo original solo permitia uno y terminaba)."""
    inicializar_cursos()  # nos aseguramos de que cursos.txt exista con los 6 cursos

    print("BIENVENIDOS")

    while True:
        mostrar_cursos()

        nombre_alumno = input("\nIngrese Nombre y Apellido del alumno (o 'salir' para terminar): ").strip()
        if nombre_alumno.lower() == "salir":
            break

        curso_elegido = input("Ingrese el nombre del curso de manera exacta: ").strip()

        cupo_maximo = obtener_cupo_maximo(curso_elegido)

        if cupo_maximo == 0:
            # El curso no existe en cursos.txt
            print("El curso ingresado no existe.")
        else:
            inscriptos_actuales = contar_inscriptos(curso_elegido)
            cupo_real_disponible = cupo_maximo - inscriptos_actuales

            if cupo_real_disponible > 0:
                registrar_inscripcion(nombre_alumno, curso_elegido)
            else:
                registrar_espera(nombre_alumno, curso_elegido)

    mostrar_estadisticas()


if __name__ == "__main__":
    iniciar_programa()

