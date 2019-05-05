from Rules import *
from DocWordCounter import *
from URLsReader import *
from HTMLReader import *


def main():
    urlDoc = URLsReader()
    rules = Rules()
    title = urlDoc.getTitle()
    #while(title is not None):
    while title is not None:
        html = HTMLReader(title)
        #Obtiene tod o el HTML del documento.
        #if not title in ["turismoespacial9.html","AM8.html","AM5.html"]:
        htmlString = html.getHtml()
        title = urlDoc.getTitle()

    # Devuelve en un string todas las palabras del documento
    #words = rules.applyRules(htmlString)

    # Se crea el objeto DocWord que se envia el titulo del archivo y el string de palabras
    #docWordCount = DocWordCounter(html, words)

    # Separa las palabras y las agrega en un diccionario por cada documento.
    #docWordCount.generateStopWordsDict()
    #docWordCount.separateWords()
    #docWordCount.generateDict()


    # Obtiene el siguiente Documento de HTML
    #title = urlDoc.getTitle()


if __name__ == '__main__':
    main()
