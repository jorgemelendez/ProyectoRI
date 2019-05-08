from Rules import *
from DocWordCounter import *
from URLsReader import *
from HTMLReader import *
from Frecuencias import *
class FileGenerator:
    numberCharacteresTerm = 30
    numberCharacteresFreq = 12
    numberCharacteresFreqNorm = 20
    numberCharacteresNumberDocument = 12
    numberCharacteresFreqInv = 20

    # Funcion para rellenar espacios para que la hilera string quede de numberCharacteres de caracteres
    def formatNumberCharacters(self, numberCharacteres, string):
        formato = '{:<'+str(numberCharacteres)+'}'
        return formato.format(string)

    # Funcion para convertir numero a caracteres
    def formatNnumberToString(self, numberCharacteres, number):
        return self.formatNumberCharacters(numberCharacteres,str(number))

    # Funcion que crea una linea del archivo
    def lineTok(self, term, freq, freqNorm):
        return self.formatNumberCharacters(self.numberCharacteresTerm, term) + ' ' + self.formatNnumberToString(self.numberCharacteresFreq,freq) + ' ' + self.formatNnumberToString(self.numberCharacteresFreqNorm, freqNorm)

    # Metodo que generar archivo .tok
    # 30 caracteres para el termino
    # 1 espacio
    # 12 espacios para la frecuencia
    # 1 espacio
    # 20 espacios para la frecuencia normalizada
    def tokGenerate(self, fileName, dictFreq, dictFreqNorm):
        for word in sorted(dictFreq.keys()):
            print(self.lineTok(word, dictFreq[word], dictFreqNorm[word]))

    # Funcion que crea una linea del archivo
    def lineVocabulary(self, term, numberDocument, freqInv):
        return self.formatNumberCharacters(self.numberCharacteresTerm, term) + ' ' + self.formatNnumberToString(
            self.numberCharacteresNumberDocument, numberDocument) + ' ' + self.formatNnumberToString(self.numberCharacteresFreqInv,
                                                                                     freqInv)
    # Metodo que genera el archivo vocabulario
    # 30 caracteres termino
    # 1 espacio
    # 12 espacios para el numero de documentos en que aparece el termino
    # 1 espacio en blanco
    # 20 caracteres para la frecuencia inversa
    def vocabularyGenerate(self, fileName, dictFreq):
        for word in sorted(dictFreq.keys()):
            print(self.lineVocabulary(word, dictFreq[word].getNumDocs(), dictFreq[word].getFrecInversa()))

def main():
    urlDoc = URLsReader()
    rules = Rules()

    title = urlDoc.getTitle()
    freq = Frecuencias()

    # while (title is not None):
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

    # print(wordDict)

    # Tiene el diccionario con las frecuencias normalizadas de cada palabra por documento.
    freqDict = freq.generateFrequency(wordDict)
    # print(freqDict)

    # Obtiene el siguiente Documento de HTML
    title = urlDoc.getTitle()

    freqInv =  freq.generateVocabDic()

    generador = FileGenerator()
    generador.tokGenerate(title, wordDict, freqDict)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    generador.vocabularyGenerate(title, freqInv)


if __name__ == '__main__':
    main()