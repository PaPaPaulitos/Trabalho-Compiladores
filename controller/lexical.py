from model.token import Token,Num, Id
from model.reserved import reserved, operators

class Lexical:
    def __init__(self,expr):
        self.__expr: str = expr
        self.__index: int = 0
        self.__stack = list()
        self.__is_digit_or_alpha = lambda x: x.isdigit() or x.isalpha()
    
    def __look_ahead(self, pos = 0) -> str | None:
        if ((self.__index + pos) <= len(self.__expr) - 1):
            return self.__expr[self.__index + pos]
        else:
            return ""

    def __parse_advance(self):
        if ((self.__index + 1) <= len(self.__expr) - 1):
            self.__index += 1

    
    def __validate_expression(self, token: str) -> None:
        if token == "(":
            if self.__look_ahead(1) in reserved:
                raise Exception("Invalid expression")
            
            self.__stack.append(token)
            return
        elif token == ')':
            if len(self.__stack) > 0:
                self.__stack.pop()
            else:
                self.__stack.append(token)
                return
        else:
            return


    def __next_token(self) -> Token:
        try:
            expression: str = ""
            while (self.__is_digit_or_alpha(self.__look_ahead())):
                if (self.__is_digit_or_alpha(self.__look_ahead())):
                    term = self.__look_ahead()
                    self.__parse_advance()
                    expression += term
            if (expression.isdigit()):
                token = Num(expression)
            elif (expression.isalpha()):
                token = Id(expression)
            elif self.__look_ahead() in reserved:
                self.__validate_expression(self.__look_ahead())
                term = self.__look_ahead()
                self.__parse_advance()
                expression = term
                token = Token(expression)
            else:
                raise Exception("Element not identified")
            return token
        except Exception as e:
            raise e

    def lexical_list(self) -> list:
        try:
            tokens: list = []
            while (self.__look_ahead() != "\n"):
                tokens.append(self.__next_token())
            
            if len(self.__stack) != 0:
                raise Exception("Unclosed parentheses")
            elif tokens[-1].tag in operators:
                raise Exception("Expression Incompleted")
            return tokens
        except Exception as e:
            raise e
        