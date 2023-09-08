'''
Considerando o IMC (índice de massa corpórea), calculado como peso/(altura*altura), exiba a situação da pessoa com base na seguinte tabela:

IMC

Situação

<= 18.5

Abaixo do peso

>18.5 e <=24.9

Peso ideal

>24.9

Acima do peso


'''

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura**2)

if (imc <= 18.5):
    print(f"IMC: {imc:.2f} - Abaixo do peso")
elif (imc <= 24.9):
    print(f"IMC: {imc:.2f} - Peso ideal")
else:
    print(f"IMC: {imc:.2f} - Acima do peso")