# previsao-do-tempo
Previsão do tempo em Python

Simples script em Python que puxa os dados da previsão do tempo do mecanismo de busca Google.

Utiliza a biblioteca requests-html:

**$ pip install requests-html**

Script modular, basta copiar a função previsao() para sua aplicação e usá-la a bel prazer.

# Forma de uso

Se você invocá-lo sem argumentos, ele retornará a previsão do tempo de sua localidade atual:

**$ python previsao.py**

É possível informar a região desejada, exemplo:

**$ python previsao.py rio de janeiro**
