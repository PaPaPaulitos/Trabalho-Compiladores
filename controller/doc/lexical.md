## Análise Léxica

A Análise Léxica foi feita utilzando a classe *Lexical* que possui os seguintes metódos.


 ```python
 def __look_ahead(self, pos = 0) -> str | None:
 ``` 

- Manda qual vai ser a próxima posição do *source code*.

Pos = Caso a posição seja uma operação como + ou - ele vai enviar a próxima operação.

 ```python
def __parse_advance(self):
 ``` 
- Avança para o próximo posição da expressão
 
 
```python
def __validate_expression(self, token: str) -> None:
```

- Vai criar uma *pilha* para verificar se os `()` estão fechando e abrindo corretamente.

```python
def __next_token(self) -> Token:
```

- Vai separa e retornar o que é `Number`, `Id` e `Token` do código.

```python
def lexical_list(self) -> list:
```

- Vai montar uma lista de Tokens e vai recusar a lista, caso a expressão seja inválida.

---