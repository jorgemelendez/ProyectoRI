from Rules import *
from DocWordCounter import *
from URLsReader import *
from HTMLReader import *
from Frecuencias import *


def main():
    urlDoc = URLsReader()
    rules = Rules()

    title = urlDoc.getTitle()
    freq = Frecuencias()

    while(title is not None):
        html = HTMLReader(title)

        # Obtiene tod o el HTML del documento.
        htmlString = html.getHtml()

        # Devuelve en un string todas las palabras del documento
        words = rules.applyRules(htmlString)

        # Se crea el objeto DocWord que se envia el titulo del archivo y el string de palabras
        docWordCount = DocWordCounter(html, words)

        # Separa las palabras y las agrega en un diccionario por cada documento.
        docWordCount.generateStopWordsDict()
        docWordCount.separateWords()
        wordDict = docWordCount.generateDict()

        print(wordDict)

        # Tiene el diccionario con las frecuencias normalizadas de cada palabra por documento.
        freqDict = freq.generateFrequency(wordDict)
        print(freqDict)

        # Obtiene el siguiente Documento de HTML
        title = urlDoc.getTitle()



if __name__ == '__main__':
    main()