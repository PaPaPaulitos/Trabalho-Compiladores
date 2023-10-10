from model.token import Token,Num, Id
from model.reserved import reserved, operators

class Lexical:
    def __init__(self,__expr):
        self.__expr: str = __expr
        self.__index: int = 0
        self.__stack = list()
    
    def __look_ahead(self, pos = 0) -> str | None:
        if ((self.__index + pos) <= len(self.__expr) - 1):
            return self.__expr[self.__index]
        else:
            return ""

    def __parse_advance(self):
        if ((self.__index + 1) <= len(self.__expr) - 1):
            self.__index += 1

    def __parse_chop(self) -> str:
        current = self.__look_ahead()
        if(current != None):
            self.__parse_advance()

        return current
    
    def __validate___expression(self, token: str) -> None:
        if token == "(":
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
            __expression: str = ""
            while (self.__look_ahead().isdigit() or self.__look_ahead().isalpha()):
                if (self.__look_ahead().isdigit() or self.__look_ahead().isalpha()):
                    term = self.__look_ahead()
                    self.__parse_advance()
                    __expression += term
            if (__expression.isdigit()):
                token = Num(__expression)
            elif (__expression.isalpha()):
                token = Id(__expression)
            elif self.__look_ahead() in reserved:
                self.__validate___expression(self.__look_ahead())
                term = self.__look_ahead()
                self.__parse_advance()
                __expression = term
                token = Token(__expression)
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
                raise Exception("__expression Incompleted")
            return tokens
        except Exception as e:
            raise e
        