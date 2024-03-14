import requests
import re

class WikiInfo:
    def __init__(self):
        self.url = "https://es.wikipedia.org/w/api.php"
        
    def obtenerInformacionAutores(self, categoria, maxAutores):
        parametros ={
            "action": "query",
            "format": "json",
            "list": "categorymembers",
            "cmtitle": "Categoría:"+categoria,
            "cmprop": "title",
            "cmlimit": maxAutores,
        }
        respuesta = requests.get(self.url, parametros)
        datos = respuesta.json()
        paginas = datos["query"]["categorymembers"]
        autores = []
        for pagina in paginas:
            autores.append(pagina)
        return autores
    
    def obtenerDescripcion(self, autor):
        parametros = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "explaintext": True,
            "titles": autor,
        }
        respuesta = requests.get(self.url, parametros)
        datos = respuesta.json()
        try:
            paginas = datos['query']['pages']
            for pagina in paginas:
                biografia = paginas[pagina]["extract"]
                
                return biografia
        except KeyError:
            return ""

    def obtenerBiografia(self, autor):
        biografia = self.obtenerDescripcion(autor)
        biografiaLimpia = re.sub(r'==.*?==', '', biografia)

        # Unir el texto resultante
        biografiaLimpia = ' '.join(biografiaLimpia.split())
        titulos = self.obtenerTitulos(biografia)
        return biografia, biografiaLimpia, titulos
    
    def obtenerTitulos(self, biografia):
        patron = re.findall(r'== (.*?) ==', biografia)
        return patron