import sys
import os
import json
import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen


def main():
    # Se define la ruta para grabar o leer el archivo

    if not os.path.exists("pokedex"):
        os.mkdir("pokedex")

    os.chdir("pokedex")

    # Se ubica por única vez el directorio o carpeta de trabajo

    # print("Directorio de trabajo "+os.getcwd())
    # input("Oprima una tecla para continuar")

    # Contador de registros a grabar en el archivo

    cont_reg = 0
    control = False

    # Se inicilizan estructuras de datos

    data = {}  # Diccionario, entre llaves: clave, valor
    data["pokemones"] = []  # Lista, corchetes, índices

    # Mientras se desee se evaluarán pokémones y se mostrarán sus datos

    while control is False:
        while True:
            pokemon = input("Introduce un pokémon: ")

            url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
            respuesta = requests.get(url)

            # Si hay un error, se pregunta si se desea continuar

            if respuesta.status_code != 200:
                print("Pokémon no encontrado")

                c_buscar_pk = " "
                c_buscar_pk = input("¿Deseas revisar otro pokémon (S/N)?")
                continuar_up_pk = c_buscar_pk.upper()
                if continuar_up_pk == "S":
                    c_buscar_pk = "S"
                elif continuar_up_pk == "N":
                    control = True
                    c_buscar_pk = "N"
                    break
                else:
                    print("Debe responder S para si y N para no")
                    continuar = " "
            else:
                datos = respuesta.json()
                break

        # Si existe el pokémon se toman los datos de la API, si no,
        # se pregunta la acción a tomar.

        try:
            # Se toman las variables requeridas del json.
            id = datos["id"]
            peso = datos["weight"]
            tamaño = datos["height"]
            habilidades = datos["abilities"]
            tipos = datos["types"]
            especies = datos["species"]["name"]
            url_imagen = datos["sprites"]["front_default"]
            imagen = Image.open(urlopen(url_imagen))

            # Se agregan datos a la lista
            # data = {}
            data["id"] = id
            data["peso"] = peso
            data["tamaño"] = tamaño
            data["habilidades"] = habilidades
            data["tipos"] = tipos
            data["especies"] = especies
            data["imagen"] = imagen

            # Se agregan los datos en el diccionario para grabar en archivo formato json

            data["pokemones"].append(
                {
                    "id": id,
                    "peso": peso,
                    "tamaño": tamaño,
                    "habilidades": habilidades,
                    "tipos": tipos,
                    "especies": especies,
                    "imagen": url_imagen,
                }
            )

            # Se muestran la lista y el diccionario de datos

            print("Lista")
            print(data)
            print("Diccionario Data")
            print(data["pokemones"])

            plt.title(datos["name"])
            imgplot = plt.imshow(imagen)
            plt.show()

        except:
            print("El pokémon no tiene imágen o no existe")

            continuar = " "

            while continuar == " ":
                continuar = input("¿Deseas revisar otro pokémon (S/N)?")
                continuar_up = continuar.upper()

                if continuar_up == "S":
                    continuar = "S"
                elif continuar_up == "N":
                    control = True
                    continuar = "N"
                    break
                else:
                    print("Debe responder S para si y N para no")
                    continuar = " "

        # Se prepara archivo de texto para grabar datos de pokémon

        if cont_reg == 0:
            with open(
                "pokemon.txt", "w"
            ) as f_archivo:  # w = Escribir o sobreescribir el primer registro
                f_archivo.write(str(id))  # id
                f_archivo.write(" ")
                f_archivo.write(str(peso))  # peso
                f_archivo.write(" ")
                f_archivo.write(str(tamaño))  # tamaño
                f_archivo.write(" ")
                f_archivo.write(str(habilidades))  # habilidades
                f_archivo.write(" ")
                f_archivo.write(str(tipos))  # tipos
                f_archivo.write(" ")
                f_archivo.write(str(especies))  # especies
                f_archivo.write(" ")
                f_archivo.write(str(imagen))  # imagen
                f_archivo.write("\n")

                cont_reg += 1
        else:
            with open(
                "pokemon.txt", "a"
            ) as f_archivo:  # a = agregar al final del archivo
                f_archivo.write(str(id))  # id
                f_archivo.write(" ")
                f_archivo.write(str(peso))  # peso
                f_archivo.write(" ")
                f_archivo.write(str(tamaño))  # tamaño
                f_archivo.write(" ")
                f_archivo.write(str(habilidades))  # habilidades
                f_archivo.write(" ")
                f_archivo.write(str(tipos))  # tipos
                f_archivo.write(" ")
                f_archivo.write(str(especies))  # especies
                f_archivo.write(" ")
                f_archivo.write(str(imagen))  # imagen
                f_archivo.write("\n")

                cont_reg += 1

        continuar = " "

        while continuar == " ":
            continuar = input("¿Deseas revisar otro pokémon (S/N)?")
            continuar_up = continuar.upper()

            if continuar_up == "S":
                continuar = "S"
            elif continuar_up == "N":
                control = True
                continuar = "N"
                break
            else:
                print("Debe responder S para si y N para no")
                continuar = " "

        # Se graba archivo json
        if cont_reg >= 0:
            with open("pokemon.json", "w") as f_json:  # w = grabar archivo json
                json.dump(data["pokemones"], f_json)

    print("Este es el archivo json registrado. ")

    with open("pokemon.json", "r") as f_lectura:  # r = archivo de solo lectura
        contenido = f_lectura.read()
        print(contenido)

    print("Fin del programa. ")


if __name__ == "__main__":
    main()
