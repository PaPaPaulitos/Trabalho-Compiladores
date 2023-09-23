# Trabalho Compiladores

Trabalho da matéria compiladores ministrada pelo professor André Lúcio na Universidade Veiga de Almeida.

---

## Objetivo do trabalho

Realizar um programa que seja capaz de fazer a tradução e análise léxica de um código fonte.

---

## PaulitosLang

É uma linguagem de programação em português com intuito de realizar cálculos matemáticos.

O seu compilador é escrito em *Python*

### Como compilar um arquivos em PaulitosLang?

Basta executar no terminal onde fica o arquivo *paulitos.py* o seguinte comando junto ao **Source Code** que termine com a extensão *.paulitos*.

```bash
python paulitos.py <nome_do_arquivo>
```


---

## Processos de Compilação

Podemos definir o processo de compilação pela seguinte imagem.

![](./Images/compilação.jpg)

### Análise Léxica

É o processo que verifica se uma palavra é aceita pela linguagem e separa as palavras aceitas em Tokens.

Exemplo a expressão

```
3 + 4 - 2
```

Ele vai verificar se cada um dos elementos da expressão existe dentro do dicionário da linguagem e separar eles, assim ficando.

```
[3] [+] [4] [-] [2]
```


### Análise Sintática

É o processo que vai organizar os Tokens em uma arvoré/string para a operação ser mandada para o Backend realizar a operação em ordem.

    A tradução deve ser capaz de recusar Tokens inválidos.

A tradução foi feita usando a fórmula ensinada em sala de aula para evitar *recursão a esquerda*

**Recusão a esquerda**

A técnica que utilizaremos para eliminar a recursão a esquerda é bem simples.

```
expr ⭢ expr + term {print('+')}
    |  expr - term {print('-')}
    | term
```

Iremos converter a expressão para uma linguagem formal para explicar.

Gramática com recursão a esquerda 
```
A ⭢ Aα | Aβ  ⭢ γR
    | Aβ | R ⭢ αR 
    | γ ⭢ ε


A = expr
α = term {print('+')}
β = term {print('-')}
γ = term
```
Gramática sem recursão a esquerda 
```
A ⭢ γR
R ⭢ αR | βR | ε

A = expr
α = term {print('+')}
β = term {print('-')}
γ = term
```

Retiraremos a possibilidade de Loop infinito usando o algoritmo para retirar a recursão a esquerda.

No exemplo dado a cima ele vai organizar em uma árvore de operações como na imagem a seguir.

![](./Images//Traducao.jpeg)

A árvore sempre percorre indo para o Nó mais a esquerda primeiro e depois imprimindo o seu operador, logo a saída será:

```
34+2-
```

### Analise Semântica


---

### Referências

- AKITA, Fábio Akita, <a href="https://www.youtube.com/watch?v=SNyh-cubxaU">Linguagem Compilada vs Interpretada | Qual é melhor?</a> , 15 de abr. de 2022.

- MONTANO, Lucas Montano, <a href="https://youtu.be/e4x4IITQvak?si=VotB_hN46C94tN0o">Explicando Linguagem Interpretada - FINALMENTE TU VAI ENTENDER</a>, 11 de set. de 2023.
