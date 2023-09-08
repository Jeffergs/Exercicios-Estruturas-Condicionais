'''
Escreva um algoritmo que pergunte o valor de uma mercadoria e qual o valor que o usuário
tem em mãos e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria.
'''

valor_mercadoria = float(input("Digite o valor da mercadoria: "))
valor_maos = float(input("Digite o valor que você tem em mãos: "))

if (valor_maos >= valor_mercadoria):
    print("O valor que tens em mãos é suficiente")
else:
    print("O valor que tens em mãos não é suficiente")

