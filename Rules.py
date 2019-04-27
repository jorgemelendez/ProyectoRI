import re

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

