class Token:
    def __init__(self,tag):
        self.tag = tag

    def __str__(self) -> str:
        return f"<{self.tag}>"
        
class Num(Token):
    def __init__(self,value):
        super().__init__("number")
        self.value = value

    def __str__(self) -> str:
        return f"<{self.tag},{self.value}>"

class Id(Token):
    def __init__(self,name):
        super().__init__("id")
        self.name = name

    def __str__(self) -> str:
        return f"<{self.tag},{self.name}>"