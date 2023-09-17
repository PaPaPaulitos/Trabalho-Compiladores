## Código

---

### Ler arquivo

A verificação se o Source File existe é feita pela classe *Readfile* que possui os seguintes metódos.

 ```python
 def __file_exists(self) -> str:
 ``` 
- Verifica se o arquivo existe no diretório em que o compilador foi chamado. 

 ```python
 def __verify_file_name(self) -> str:
 ``` 
- Verifica se o arquivo é da extensão *.paulitos*

 ```python
 def source_code(self) -> str:
 ``` 
- Lê o que foi escrito no arquivo e envia para o processo de compilação. 


---

### Análise Léxica

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
def parse_term(self) -> str:
``` 

- Verifica se o Token é um número

---

### Tradução

A tradução foi feita utilzando a classe *Parse* que possui os seguintes metódos.

```python
def parse_expr(self)-> str | None:
``` 

- Vai montar a expressão traduziada

```python
def parse(self, source) -> str:
 ``` 

- Método que vai iniciar a tradução da expressão e retornar uma expressão traduzida para o analisador léxico


Source = Expressão que foi escrita no Source Code
