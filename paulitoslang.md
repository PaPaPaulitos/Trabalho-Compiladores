# PaulitosLang

![Logo Paulitos Lang](./Images/paulitoslang_logo.png)

É uma linguagem de programação em português com intuito de realizar cálculos matemáticos.

O seu compilador é escrito em *Python*

Sua grámatica atual é:

```
expr: term '+' term  
    | term '-' term 
    | term
    ;

term:
    | factor '*' factor
    | factor '/' factor
    | factor 
    ;

factor:
    | '(' expr ')'
    | IDENTIFER
    | NUMBER_LIT
    ;

IDENFIER: { a..z A..Z }+
NUMBER_LIT: { 0..9 }+
```

## Qual é a extensão do PaulitosLang?

A extensão da PaulitosLang é *.paulitos*

## Como compilar um arquivos em PaulitosLang?

Basta executar no terminal onde fica o arquivo *paulitos.py* o seguinte comando junto ao **Source Code** que termine com a extensão *.paulitos*.

```bash
python paulitos.py <nome_do_arquivo>.paulitos
```

## Outros meios de executar um código da PaulitosLang

- Você pode entrar na pasta `codigo_fonte` e editar o `main.paulitos`para a expressão que você quer.

- Após isso é só clicar no arquivo `PaulitosLang` dentro do diretório.

> Atenção só funciona para Windows

![Executando PaulitosLang](./Images/executando_paulitoslang.png)