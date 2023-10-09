from model.token import Token, Id
from model.symTable import SymTable

from controller import lexical

operators = ["+", "-", "*", "/"]

class Parser:
    def __init__(self):
        self.__lexical = lexical.Lexical()
        self.__translated = list()
        self.__symbol_table = SymTable()


    def parse_expr(self)-> list | None:
        t1 = self.__lexical.parse_term()
        self.__translated.append(t1)

        while(self.__lexical.look_ahead() in operators):
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

"""  
    def parse_term(self) -> Num | Id:
        try:
            expression: str = ""
            while (self.look_ahead().isdigit() or self.look_ahead().isalpha()):
                if (self.look_ahead().isdigit() or self.look_ahead().isalpha()):
                    term = self.look_ahead()
                    self.parse_advance()
                    expression += term
            if (expression.isdigit()):
                token = Num(expression)
            elif (expression.isalpha()):
                token = Id(expression)
            return token
        except Exception as e:
            raise e("Sintax error")

    def part_factor(self) -> Num | Id:
"""  