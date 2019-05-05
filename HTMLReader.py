import chardet
import re
class HTMLReader:
    def __init__(self, docName):
        self.fileName = './Coleccion/' + docName
        #print(self.fileName)
        # Se tiene que cambiar el tipo de encoding del archivo y
        # se tiene que ignorar ciertos errores de caracteres que dice que no existen.
        self.file = open(self.fileName, "rb")


    # Metodo que devuelve todito el html del archivo
    def getHtml(self):
        read=self.file.read()
        try:
            html = read.decode(chardet.detect(read)["encoding"])
        except:
            try:
                html = read.decode("UFT-8")
            except:
                try:
                    html = read.decode("ISO-8859-1")
                except:
                    print("\n\n\n\n-------------------------------------------\n\n\n\n")
        encode = re.findall("(?:(?<=charset\=\")[^\"]+?(?=\"))|(?:(?<=charset\=)[^\"]+?(?=\"))", html)
        if encode:
                encode=encode[0]
        else:
                encode="uft-8"
        print(encode)
        self.file.close()
        self.file = open(self.fileName, "rb")
        html=self.file.read().decode(encode)
        return html
