from model.token import Token,Num, Id
from model.reserved import reserved

class Lexical:
    def __init__(self,expr):
        self.expr: str = expr
        self.index: int = 0
        self.stack = list()
    
    def look_ahead(self, pos = 0) -> str | None:
        if ((self.index + pos) <= len(self.expr) - 1):
            return self.expr[self.index]
        else:
            return ""

    def parse_advance(self):
        if ((self.index + 1) <= len(self.expr) - 1):
            self.index += 1

    def parse_chop(self) -> str:
        current = self.look_ahead()
        if(current != None):
            self.parse_advance()

        return current
    
    def validate_expression(self, token: str) -> None:
        if token == "(":
            self.stack.append(token)
            return
        elif token == ')':
            if len(self.stack) > 0:
                self.stack.pop()
            else:
                self.stack.append(token)
                return
        else:
            return


    def next_token(self) -> Token:
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
            elif self.look_ahead() in reserved:
                self.validate_expression(self.look_ahead())
                term = self.look_ahead()
                self.parse_advance()
                expression = term
                token = Token(expression)
            else:
                raise Exception("Invalid expression")
            return token
        except Exception as e:
            raise e

    def lexical_list(self) -> list:
        try:
            tokens: list = []
            while (self.look_ahead() != "\n"):
                tokens.append(self.next_token())
            if len(self.stack) != 0:
                raise Exception("Invalid expression")
            return tokens
        except Exception as e:
            raise e
        
