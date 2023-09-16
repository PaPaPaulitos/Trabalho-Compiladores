from model.parser import Parser


if __name__ == '__main__':
    parser = Parser()

    input = input("> ")

    try:
        expression = parser.parse(input)
        print(expression)
    except Exception as e:
        print(e)
    



