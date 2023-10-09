from controller.parser import lexical
from controller.readfile import Readfile

if __name__ == '__main__':
    file =  Readfile()
    expr = file.source_code()
    print(f'O código retirado do arquivo foi {expr}')

    try:
        expression = lexical.Lexical(expr).lexical_list()
        for token in expression:
            print(token, end=" ")
    except Exception as e:
        print(e)
    



