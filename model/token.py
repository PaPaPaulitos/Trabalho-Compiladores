class Token:
    def __init__(self,tag):
        self.tag: str = tag

    def __str__(self) -> str:
        return f"<{self.tag}>"
        
class Num(Token):
    def __init__(self,value):
        super().__init__("number")
        self.value: str = value

    def __str__(self) -> str:
        return f"<{self.tag},{self.value}>"

class Id(Token):
    def __init__(self,name):
        super().__init__("id")
        self.name: str = name

    def __str__(self) -> str:
        return f"<{self.tag},{self.name}>"