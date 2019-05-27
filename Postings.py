from WtdReader import *
from FileGenerator import *

class Postings:

    # Metodo que devuelve un diccionario de Postings
    # Llave: termino, aliasDocumeto
    # Valor: peso
    def getDicPostings(self, filesName):
        #generator = FileGenerator()
        dicPostings = dict()
        for file in filesName:
            wtdReader = WtdReader(file)
            dicWtd = wtdReader.getDicWtd()
            for word in dicWtd:
                llave = word, file
                dicPostings[llave] = dicWtd[word]
        for posting in dicPostings:
            print(str(posting) + " " + str(dicPostings[posting]))

    def generatePostings(self, filesName):
        dicPostings = self.getDicPostings(filesName)
        generator = FileGenerator()
        generator.postings(dicPostings)



# Main para prueba ver que genere los archivos .wtd
if __name__ == '__main__':
    filesName = '1_AP', '1_CT'
    weights = Postings()
    weights.generatePostings(filesName)