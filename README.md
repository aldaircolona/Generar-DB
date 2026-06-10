# Generador de Datos Sintéticos en Python

## Descripción

Este proyecto consiste en una herramienta desarrollada en Python para la generación de grandes volúmenes de datos sintéticos. Su objetivo es facilitar la creación de conjuntos de datos de prueba para experimentos, análisis de rendimiento, validación de algoritmos y simulaciones en bases de datos.

Los datos generados incluyen información personal ficticia, como nombres y números de documento, almacenados en archivos CSV para su posterior procesamiento o importación en sistemas gestores de bases de datos.

## Características

Generación masiva de registros sintéticos.
Creación de nombres aleatorios a partir de listas predefinidas.
Generación de números de identificación únicos (DNI de 8 dígitos).
Exportación directa a archivos CSV.
Diseño escalable para conjuntos de datos de gran tamaño.

## Tecnologías Utilizadas

- Python 3.12
- Módulo csv
- Módulo random
- Módulo os

## Estructura del Proyecto

```text
Proyecto/
│
├── data/
│ └── personas.csv
│
├── data inicial/
│ ├── apellido.csv
│ ├── nombres-femenino.csv
│ └── nombres-masculino.csv
│
├── main.py
│
├── .gitignore
└── README.md
```

## Funcionamiento

Se cargan las listas de nombres y apellidos desde archivos CSV ubicados en el directorio data inicial.
Se generan registros aleatorios combinando dichos valores.
Se asigna un identificador único a cada registro.
Los registros se escriben directamente en un archivo CSV que se ubicará en el directorio data.

## Ejecución

```bash
python main.py
```

## Formato de Salida

Ejemplo de archivo generado:

```text
dni,nombres,apellidos,genero
64133521,Armando Reynaldo,Campos Dueñas,M
87783560,Leslie Elisa,Zevallos Molina,F
50675327,Viviana Valentina,Delgado Garrido,F
```

## Casos de Uso

Pruebas de rendimiento en bases de datos.
Evaluación de algoritmos de búsqueda y filtrado.
Simulación de grandes volúmenes de información.
Desarrollo y validación de aplicaciones.
Investigación académica relacionada con procesamiento de datos.

## Consideraciones

Los datos generados son completamente ficticios y no representan personas reales. El proyecto está destinado exclusivamente a fines educativos, de investigación y pruebas técnicas.

## Autor

Desarrollado como proyecto de generación de datos sintéticos utilizando Python.
