class Frecuencias:

    def __init__(self):
        # Diccionario que guarda la palabra y la suma de las veces que sale en los documentos.
        self.dictionary = dict()


    # Metodo que genera el diccionario de frecuencias
    # Recibe como parametro el diccionario de cada documento.
    # Devuelve un diccionario que los keys son las palabras del documento y los values
    def generateFrequency(self, dictionary):
        highestWordCount = 0
        highestWord = None

        freqDict = dict()
        # Buscamos la plabra con mayor frecuencia del documento.
        for word in dictionary:

            # Revisa que el diccionario general tenga la palabra y suma la cantidad que tiene
            # o sino la agrega.
            if word in self.dictionary:
                value = self.dictionary[word]
                print(word)
                print(dictionary[word])
                value += dictionary[word]
                print(value)
                print('-----------')
                self.dictionary[word] = value
            else:
                self.dictionary[word] = dictionary[word]

            # Busca la palabra con mayor peso en el documento
            if (dictionary[word] > highestWordCount):
                highestWordCount = dictionary[word]
                highestWord = word

        for word in dictionary:
            freq = dictionary[word]/highestWordCount
            freqDict[word] = freq

        return freqDict


    # Metodo que agrega las palabras al diccionario general y suma las veces que aparecen.
    def generateDict(self):
        return 0


    def getDictionary(self):
        return self.dictionary['autor']
