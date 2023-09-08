'''
Escreva um algoritmo que verifique se um número inteiro digitado pelo usuário é ou
não divisível por 5.
'''

num = int(input("Digite um número inteiro: "))

if (num % 5 == 0):
    print("O número é divisível por 5")
else:
    print("O número não é divisível por 5")