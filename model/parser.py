class Parser:
    def __init__(self):
        self.source: str
        self.index = 0

    """
    
        Manda qual vai ser a próxima posição a sertransformada em um Token

        Pos = Caso o  Token seja uma operação como + ou - ele vai enviar o próximo Token
    """

    def look_ahead(self, pos = 0) -> str | None:
        if ((self.index + pos) <= len(self.source) - 1):
            return self.source[self.index]
        else:
            return ""

    """

        Avança para o próximo Token
    
    """
    def parse_advance(self):
        if ((self.index + 1) <= len(self.source) - 1):
            self.index += 1

    """
    
    Envia o próximo Token

    """
    def parse_chop(self) -> str:
        current = self.look_ahead()
        if(current != None):
            self.parse_advance()

        return current

    """
    
    Verifica se o Token é um número

    """
    def parse_term(self) -> str:
        try:
            if (self.look_ahead().isdigit()):
                term = self.look_ahead()
                self.parse_advance()
                return term
        except Exception as e:
            raise Exception("Sintax error")

    """
    
    Vai montar a expressão traduziada

    """
    def parse_expr(self)-> str | None:
        translated = ''
        t1 = self.parse_term()
        translated += t1

        while(self.look_ahead() == '+' or self.look_ahead() == '-'):
            op = self.parse_chop()
      
            t2 = self.parse_term()
            translated += f'{t2}{op}'

        return translated

    """
    
    Metodo que vai iniciar a tradução da expressão e retornar uma expressão traduzida para o analisador léxico


    Source = Expressão que foi escrita no Source Code
    
    """

    def parse(self, source) -> str:
        self.source = source
        try:
            return self.parse_expr()
        except Exception as e:
            raise Exception("Sintax error")
    