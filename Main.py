from URLsReader import *
from HTMLReader import *

# Para hacer el parser de HTML este link puede servir: https://stackoverflow.com/questions/11804148/parsing-html-to-get-text-inside-an-element


def main():
    toy = URLsReader()

    title = toy.getTitle()
    while(title is not None):
        print(title)
        html = HTMLReader(title)
        title = toy.getTitle()
        html.printHtml()


if __name__ == '__main__':
    main()