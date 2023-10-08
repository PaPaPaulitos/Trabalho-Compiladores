from model.token import Token, Id
from model.symTable import SymTable

from controller import lexical

class Parser:
    def __init__(self):
        self.__lexical = lexical.Lexical()
        self.__translated = list()
        self.__symbol_table = SymTable()


    def parse_expr(self)-> list | None:
        t1 = self.__lexical.parse_term()
        self.__translated.append(t1)

        while(self.__lexical.look_ahead() == '+' or self.__lexical.look_ahead() == '-' or self.__lexical.look_ahead() == '*' or self.__lexical.look_ahead() == '/'):
            op = self.__lexical.parse_chop()
            token = Token(op)
            t2 = self.__lexical.parse_term()
            self.__translated.append(t2)
            self.__translated.append(token)
            

        return self.__translated

    def parse(self, expr) -> str:
        self.__lexical.expr = expr
        try:
            return self.parse_expr()
        except Exception as e:
            raise Exception("Sintax error")
    