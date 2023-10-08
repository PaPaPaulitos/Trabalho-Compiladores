from model.token import Token

from controller import lexical

class Parser:
    def __init__(self):
        self.__lexical = lexical.Lexical()
        self.__translated = list()


    def parse_expr(self)-> list | None:
        t1 = self.__lexical.parse_term()
        self.__translated.append(t1)

        while(self.__lexical.look_ahead() == '+' or self.__lexical.look_ahead() == '-'):
            if(self.__lexical.look_ahead() == '+'):
                token = Token('+')
            elif(self.__lexical.look_ahead() == '-'):
                token = Token('-')
            op = self.__lexical.parse_chop()
            t2 = self.__lexical.parse_term()
            self.__translated.append(t2)
            self.__translated.append(op)
            

        return self.__translated


    def parse(self, expr) -> str:
        self.__lexical.expr = expr
        try:
            return self.parse_expr()
        except Exception as e:
            raise Exception("Sintax error")
    