import chardet
class HTMLReader:
    def __init__(self, docName):
        self.fileName = './Coleccion/' + docName
        print(self.fileName)
        # Se tiene que cambiar el tipo de encoding del archivo y
        # se tiene que ignorar ciertos errores de caracteres que dice que no existen.
        self.file = open(self.fileName, "rb")


    # Metodo que devuelve todito el html del archivo
    def getHtml(self):
        read=self.file.read()
        print(chardet.detect(self.file.read()))
        try:
            html = read.decode(chardet.detect(read)['encoding'])
        except:
            html = read.decode("ISO-8859-1")
        #print(html)
        return html
