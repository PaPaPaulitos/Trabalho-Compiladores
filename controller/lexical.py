from model.token import Num

class Lexical:
    def __init__(self):
        self.expr: str
        self.index = 0
    
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
    
    def peek(self) -> str | None:
        pass


    def parse_term(self) -> Num:
        try:
            number = ""
            while (self.look_ahead().isdigit()):
                if (self.look_ahead().isdigit()):
                    term = self.look_ahead()
                    self.parse_advance()
                    number += term
            token = Num(number)
            print(f"< number ,{token.value}>", end=" ")
            return number
        except Exception as e:
            raise e("Sintax error")
