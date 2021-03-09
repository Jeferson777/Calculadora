"""
Aplicação Calculadora.
"""

# Importando um módulo com uma Classe do pacote calculo:
from calculos.classCalculo import Calculos

# Recebendo entrada de dados:
a = int(input('Insira um número: '))
operador = input('Insira um operador: ')
b = int(input('Insira outro número: '))

# Instanciando a "Classe" e inserindo as variáveis com os dados de parâmetros:
soma = Calculos(a, operador, b)

# Condicional com métodos da classe:
if operador == '+':
    print(Calculos.somar(soma))  # Inserindo a variável instanciada.
elif operador == '-':
    print(Calculos.subtrair(soma))
elif operador == '*':
    print(Calculos.multiplicar(soma))
elif operador == '/':
    print(Calculos.dividir(soma))
elif operador == '//':
    print(Calculos.quociente(soma))
elif operador == '%':
    print(Calculos.resto(soma))
else:
    print(Calculos.potenciacao(soma))
