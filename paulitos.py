from controller.parser import lexical
from controller.readfile import Readfile

if __name__ == '__main__':
    #file =  Readfile()
    #expr = file.source_code()

    try:
        expression = lexical.Lexical("(exp+3)*4/2\n").lexical_list()
        for token in expression:
            print(token, end=" ")
    except Exception as e:
        print(e)
    



