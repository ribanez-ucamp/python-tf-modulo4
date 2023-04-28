# pyhton-tf-mod4
# Repositorio para el trabajo final del módulo 4

![](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

![](https://images.wikidexcdn.net/mwuploads/wikidex/thumb/4/43/latest/20190406170624/Bulbasaur.png/200px-Bulbasaur.png){width='100px'}

<img src="https://pbs.twimg.com/media/EiAuAS8VoAA1-4T?format=jpg&name=large" alt="JuveR" width="300px">


Objetivos

Aprender a consumir una API web pública con la librería requests. En este caso, se realiza a través de la URL:
    
    "https://pokeapi.co/api/v2/pokemon/"

Dominar la gestión de códigos de status de una API así como el manejo de los resultados:

    respuesta.status_code

Crear un archivo dentro del sistema operativo y guardar información en él:

    Se crea un archivo .txt

    with open(
        "pokemon.txt", "w"
    ) as f_archivo:  # w = Escribir o sobreescribir el primer registro

    y un archivo .json

    with open("pokemon.json", "w") as f_json:  # w = grabar archivo json
        json.dump(data["pokemones"], f_json)


Aprender un poco del mundo Pokémon

https://pokeapi.co/ y Talend API Tester

{
        "abilities":[
        {
        "ability":{
        "name": "dragons-maw",
        "url": "https://pokeapi.co/api/v2/ability/263/"
        },
        "is_hidden": false,
        "slot": 1
        }
        ],
        "base_experience": 290,
        "forms":[
        {
        "name": "regidrago",
        "url": "https://pokeapi.co/api/v2/pokemon-form/895/"
        }
        ],
        .
        .
        .
}

Requisitos:

El proyecto debe realizarse de forma individual.

Entregar el link de su repositorio público de GitHub donde en el README.md detallen como cómo lo hicieron, qué bibliotecas necesitaría otro usuario para ejecutar el proyecto, mostrando imágenes de muestra de algún resultado de búsqueda de un pokémon y describiendo qué han aprendido en este módulo.

Las bibliotecas requeridas son:

import sys: Provee acceso a algunas variables usadas o mantenidas y a funciones que interactúan estrechamente con el intérprete.
import os: Nos permite acceder a funcionalidades dependientes del Sistema Operativo.
import json: Nos sirve para representar y almacenar información relacionado con un diccionario de Python, es decir, una estructura de datos (objeto) que se almacena en la memoria del dispositivo mientras se ejecuta el programa de Python.
import requests: Sirve para realizar solicitudes http cuando se está desarrollando el lado del servidor de una página web.
import matplotlib.pyplot: Open source que permite crear visualizaciones de datos en forma gráfica
from PIL import Image: Agrega soporte para abrir, manipular y guardar muchos formatos de archivos de imágenes diferentes.
from urllib.request import urlopen: Define funciones y clases que ayudan en la apertura de URLs (la mayoría http)

Entregables:

Entregar un repositorio del código en GitHub con los siguientes archivos:

README.md : Donde explicarán su proyecto y lo que han aprendido como previamente se mencionó

Archivo .py: El código funcional comentado de su proyecto

Carpeta “pokedex”: Una carpeta con un archivo .json dentro para demostrar que han podido guardar información en un archivo con éxito.

RESUMEN DE LA FUNCIONALIDAD

1. Se define la ruta para grabar o leer el archivo pokedex.
2. Se inicializa un contador de registros a grabar en el archivo.
3. Se inicilizan estructuras de datos: Diccionario y lista.
4. Mientras se desee se evaluarán pokémones y se mostrarán sus datos.
5. Si hay un error al indicar el pokémon, se pregunta si se desea continuar.
6. Si existe el pokémon se toman los datos de la API, si no, se pregunta la acción a tomar.
7. Se toman de la información del pokémon, las variables requeridas del json.
8. Se agregan datos a la lista.
9. Se agregan los datos en el diccionario para grabar en archivo formato json.
10. Se muestran la lista y el diccionario de datos.
11. Se prepara archivo de texto para grabar datos de pokémon.
12. Se graba archivo json.
13. Se utilizan los siguientes parámetros paa grabar:
    a. w = Escribir o sobreescribir el primer registro.
    b. a = agregar al final del archivo.
    c. w = grabar archivo json.
