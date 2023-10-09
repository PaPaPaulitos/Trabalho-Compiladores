# Ler arquivo

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