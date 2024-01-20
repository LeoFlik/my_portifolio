"""
Exercício Análise de Números

Objetivo: Desenvolver um programa que solicita ao usuário a entrada de 
um número e, com base nesse número, realiza as seguintes operações:

    1. Mostrar o número informado.
    2. Informar se o número é par ou ímpar.
    3. Informar se o número é positivo, negativo ou zero.
    4. Se o número for positivo, calcular e mostrar sua raiz quadrada.

"""

number = int(input("Please,choose a number: "))

if number == 0:
    print("Your number is zero")
elif number %2 == 0:
    print("Your number is even")
else:
     print ('Your number is odd')


if number == 0:
    print("Your number is", number)
elif number < 0:
    print("Your number is negative")
else:
    square_root = number**0.5
    print("Your number is positive\nIts square root is:", format(square_root, ".2f"))
