from controller.parser import Parser
from controller.readfile import Readfile

if __name__ == '__main__':
    #file =  Readfile()
    parser = Parser()
    #expr = file.source_code()

    try:
        expression = parser.parse("33+77\n") # Colocar depois o expr aqui [NÃO ESQUECER PAULO]
        print(expression)
    except Exception as e:
        print(e)
    



