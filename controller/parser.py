from controller import lexical

class Parser:
    def __init__(self):
        self.__lexical = lexical.Lexical()


    def parse_expr(self)-> str | None:
        translated = ''
        t1 = self.__lexical.parse_term()
        translated += t1

        while(self.__lexical.look_ahead() == '+' or self.__lexical.look_ahead() == '-'):
            op = self.__lexical.parse_chop()
      
            t2 = self.__lexical.parse_term()
            translated += f'{t2}{op}'

        return translated


    def parse(self, expr) -> str:
        self.__lexical.expr = expr
        try:
            return self.parse_expr()
        except Exception as e:
            raise Exception("Sintax error")
    