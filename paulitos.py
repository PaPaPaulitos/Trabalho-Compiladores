from controller.parser import Parser
from controller.readfile import Readfile

if __name__ == '__main__':
    file =  Readfile()
    parser = Parser()
    expr = file.source_code()

    try:
        expression = parser.parse(expr)
        print(expression)
    except Exception as e:
        print(e)
    



