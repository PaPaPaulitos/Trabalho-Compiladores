from model.token import Token

class SymTable:
    def __init__(self):
        self.__hash_table = dict()

    def hasToken(self, key) -> bool :
        if key in self.__hash_table:
            return True
        else:
            return False
        
    def getExpression(self,key) -> Token:
        return self.__hash_table[key]

    def insertToken(self, key, value):
        self.__hash_table[key] = value
  
    