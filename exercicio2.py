'''
Um estacionamento cobra R$ 5,00 por hora porém possui um teto de cobrança máxima de R$ 35,00,
 independente do número de horas. Escreva um algoritmo que pergunte ao usuário qual foi o
 período de permanência em horas e escreva na tela o total a pagar.
'''

perm_horas = float(input("Digite qual foi o período de permanência no estacionamento: "))

if (perm_horas >= 7):
    print("Valor a pagar é de R$35.00")
else:
    valor_pagar = perm_horas * 5.00
    print(f"Valor a pagar é de R${valor_pagar:.2f}")