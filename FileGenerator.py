class FileGenerator:
    numberCharacteresTerm = 30
    numberCharacteresFreq = 12
    numberCharacteresFreqNorm = 20

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
        print ("hola")

def main():
    generador = FileGenerator()
    print('...' + generador.lineTok('TerminoHola', 14.1234567890, 7.1234567890) + '...')

if __name__ == '__main__':
    main()