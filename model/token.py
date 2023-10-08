class Token:
    def __init__(self,tag):
        self.tag = tag
        
class Num(Token):
    def __init__(self,value):
        self.value = value

class Id(Token):
    def __init__(self,name):
        self.name = name