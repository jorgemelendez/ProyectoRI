import chardet
import re

import csv 
import requests 
import xml.etree.ElementTree as ET 

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
        encode = re.findall("\<.*?meta.*?charset.*?\>", html.lower())
        if encode != []:
              encode = re.findall("(?<=[^a-z\-0-9])[a-z\-0-9]+(?=[^a-z\-0-9])", encode[0])
              if "charset" in encode and encode.index("charset")+1 < len(encode):
                    encode=encode[encode.index("charset")+1]
              else:
                    encode="UTF-8"
        else:
              encode="UTF-8"
        #print(encode.upper())
        self.file.close()
        try:
              self.file = open(self.fileName, "rb")
              html=self.file.read().decode(encode)
        except:
              try:
                    html=self.file.read().decode("ISO-8859-1")
              except:
                    html=self.file.read().decode("UTF-8")

        return html
