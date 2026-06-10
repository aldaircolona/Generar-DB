from pathlib import Path
import random
import csv

# =================================================
# LEER DATA INICIAL
# =================================================

def cargar_lista(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        
        lista = [linea.strip() for linea in archivo if linea.strip()]
        return lista


# =================================================
# GENERAR DATA PERSONA
# =================================================

def generar_dni_unico(dnis_generados : set):
    while True:
        dni = str(random.randint(10000000, 99999999))

        if dni not in dnis_generados:
            dnis_generados.add(dni)
            return dni
        
def generar_persona(nombres_masculino, nombres_femenino, apellidos, dnis_generados):

    # 50% hombre - 50% mujer
    es_masculino = random.random() < 0.5

    genero = 'M' if es_masculino else 'F'

    lista_nombres = (
        nombres_masculino
        if es_masculino
        else nombres_femenino
    )

    # 85% dos nombres; 15% un nombre
    if random.random() < 0.85:
        nombre1 = random.choice(lista_nombres)
        nombre2 = random.choice(lista_nombres)

        nombres = f"{nombre1} {nombre2}"

    else:
        nombres = random.choice(lista_nombres)

    # apellidos
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)

    apellidos_completos = f"{apellido1} {apellido2}"

    dni = generar_dni_unico(dnis_generados)

    return [
        dni,
        nombres,
        apellidos_completos,
        genero
    ]


# =================================================
# ESCRIBIR DATA FINAL
# =================================================
def escribir_data_final(ruta_personas, total_de_registros, nombres_masculino, nombres_femenino, apellidos, dnis_generados):
    with open(
    ruta_personas,
    "w",
    newline="",
    encoding="utf-8"
    ) as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([
            "dni",
            "nombres",
            "apellidos",
            "genero"
        ])

        for _ in range(total_de_registros):
            persona = generar_persona(nombres_masculino, nombres_femenino, apellidos, dnis_generados)
            writer.writerow(persona)


# =================================================
# PROGRAMA PRINCIPAL
# =================================================
def main():
    data_inical_ruta_base = Path.cwd() / Path("data inicial")
    ruta_nombres_masculino = data_inical_ruta_base / "nombres-masculino.csv"
    ruta_nombres_femenino = data_inical_ruta_base / "nombres-femenino.csv"
    ruta_apellidos = data_inical_ruta_base / "apellidos.csv"

    nombres_masculino = cargar_lista(ruta_nombres_masculino)
    nombres_femenino = cargar_lista(ruta_nombres_femenino)
    apellidos = cargar_lista(ruta_apellidos)

    dnis_generados = set()

    data_final_ruta_base = Path.cwd() / Path("data")
    ruta_personas = data_final_ruta_base / "personas.csv"

    TOTAL_DE_REGISTROS = 100_000
    escribir_data_final(ruta_personas, TOTAL_DE_REGISTROS, nombres_masculino, nombres_femenino, apellidos, dnis_generados)
    
    print("Proceso terminado")


main()