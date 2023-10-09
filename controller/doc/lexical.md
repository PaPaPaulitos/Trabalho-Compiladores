## Análise Léxica

A Análise Léxica foi feita utilzando a classe *Lexical* que possui os seguintes metódos.


 ```python
 def look_ahead(self, pos = 0) -> str | None:
 ``` 

- Manda qual vai ser a próxima posição a sera transformada em um Token.

Pos = Caso o  Token seja uma operação como + ou - ele vai enviar o próximo Token.


 ```python
def parse_advance(self):
 ``` 
- Avança para o próximo Token
 
```python
def parse_chop(self) -> str:
``` 
- Envia o próximo Token


```python
def validate_expression(self, token: str) -> None:
```

- Vai criar uma *pilha* para verificar se os `()` estão fechando e abrindo corretamente.

```python
def next_token(self) -> Token:
```

- Vai separa e retornar o que é `Number`, `Id` e `Token` do código.

```python
def lexical_list(self) -> list:
```

- Vai montar uma lista de Tokens e vai recusar a lista, caso a expressão seja inválida.

---