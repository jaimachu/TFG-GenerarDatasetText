from WikiInfo import WikiInfo
import re
import os

mapa = {} # Mapa que contiene como clave el nombre del famoso y el valor serán los apartados que desarrollara la Chati

if __name__ == '__main__':
    wiki = WikiInfo()
    listaEntradas = []

    # Leemos del fichero de entrada
    with open("entrada.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    listaEntradas = contenido.split("\n")

    listaPersonas = []
    for nombre in listaEntradas:
        personas = wiki.obtenerInformacionAutores(nombre, 100)
        comienzoArchivoWiki = len(os.listdir("Textos-Wikipedia"))
        comienzoArchivoGPT = len(os.listdir("Preguntas-GPT/"))
        for persona in personas:
            if not (persona['title'].__contains__("Categoría:")):
                famoso = persona['title']
                listaPersonas.append(persona['title'])
                biografiaLimpia, biografia, listaTitulos = wiki.obtenerBiografia(famoso)

                # Escribimos el contenido de la Wikipedia en un archivo
                with open("Textos-Wikipedia/text"+str(comienzoArchivoWiki)+".txt", "w", encoding="utf-8") as archivo:
                    archivo.write(biografia)
                comienzoArchivoWiki = comienzoArchivoWiki + 1

                cadenaTitulos = ""
                for titulo in listaTitulos:
                    cadenaTitulos = cadenaTitulos + titulo + ", "
                cadena = "Quiero que me hagas un texto que explique la vida de "+famoso+" donde la expliques a partir de estos índices: " + cadenaTitulos

                # Escribimos las preguntas que le haremos a la Chati
                with open("Preguntas-GPT/text"+str(comienzoArchivoGPT)+".txt", "w", encoding="utf-8") as archivo:
                    archivo.write(cadena)
                comienzoArchivoGPT = comienzoArchivoGPT + 1
