import re
from URLsReader import *
from HTMLReader import *

from unicodedata import normalize

# Clase para implementar las reglas que se va a utilizar
class Rules:
    maxLength = 30

    #Regla para eliminar las etiquetas html
    def removeTagsHTML(self, stringDoc):
        return re.sub(r'<[^>]*?>', '', stringDoc)

    #Regla para eliminar palabras de mas de 30 caracteres
    def removeMaxLength(self, stringDoc):
        return re.sub(r'[^> ]{30,}', '', stringDoc)

    #Regla para pasar el texto a minuscula
    def toLowerCase(self, stringDoc):
        return stringDoc.lower()

    #Regla para quitar caracteres que no sean a-z, A-Z, 0-9, _
    def removeCharactersInvalid(self, stringDoc):
        return re.sub(r'[^\wa-zA-Z0-9_ ]', '', stringDoc)

    #Regla para quitar tildes
    def removeTick(self, stringDoc):
        return normalize('NFC',
                         re.sub(r"([^n\u0300-\u036f]|ñ(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
                                r"\1",
                                normalize("NFD", stringDoc),
                                0,
                                re.I)
                         )

    #Regla para eliminar palabras que son alfanumericas
    def removeIfStartWithNumber(self, stringDoc):
        #Hay que dejar ese espacio al final para que indique que es hasta que finalizo la palabra
        return re.sub(r'[\d]+[a-zA-Z_]+? ', '', stringDoc)

    #Regla para dejar los numeros hasta el 999,999
    def removeNumberBiggerThan(self, stringDoc):
        return re.sub(r'[\d]{7,}(,[\d]+)?', '', stringDoc)

def main():
    toy = URLsReader()

    title = toy.getTitle()
    #print(title)
    html = HTMLReader(title)
    html.printHtml()


    rules = Rules()
    doc = "55555 666666 7777777 333 4444 666666,99 999999,99999 1000000,00"
    print(doc)
    print("\n\n")
    print(rules.removeNumberBiggerThan(doc))


if __name__ == '__main__':
    main()