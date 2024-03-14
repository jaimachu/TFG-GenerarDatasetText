from openai import OpenAI
import os

def leerPreguntas(nombre):
    with open("preguntas"+nombre+".txt", "r", encoding="utf-8") as file:
        contenido = file.read()
    listaPreguntas = contenido.split("\n")
    return listaPreguntas

def preguntarChati(pregunta):
    respuesta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": pregunta},
        ]
    )
    return respuesta.choices[0].message.content

if __name__ == '__main__':
    pathSalida = "Dataset/Fake-Jaime/" # Lugar donde se van a ubicar las respuestas de la chati

    # IMPORTANTE. Reemplazar este token por el vuestro propio
    """
    apiKey = "Mi Token" 
    cliente = OpenAI(api_key=apiKey)
    nombre = "Jaime" # Cambiar por la persona que esté ejecutando el script
    """

    listaPreguntas = leerPreguntas(nombre)
    contadorArchivo = len(os.listdir(pathSalida))
    for pregunta in listaPreguntas:
        respuesta = preguntarChati(pregunta)
        with open(pathSalida+"text"+str(contadorArchivo)+".txt", "w", encoding="utf-8") as file:
            file.write(respuesta)
        contadorArchivo = contadorArchivo + 1