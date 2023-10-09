
# Tradução

A tradução foi feita utilzando a classe *Parse* que possui os seguintes metódos.

```python
def parse_expr(self)-> str | None:
``` 

- Vai montar a expressão traduziada

```python
def parse(self, source) -> str:
 ``` 

- Método que vai iniciar vai retornar a árvore binária que vai ser usada para realizar as operações.


Source = Expressão que foi escrita no Source Code

```python
def parse_term(self) -> str:
``` 

- Vai ordernar a lista a árvore binária de acordo com a ordem até achar um operador que tenha prioridade.

```python
def parse_fact(self) -> str:
``` 

- Quando o `parse_term` encontrar um operador com prioridade vai ser chamada essa função para reordenar a árvore colocando a prioridade desse operador.

---