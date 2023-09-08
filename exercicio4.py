'''
As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
calcule e escreva o custo total da compra.
'''

macas_comparadas = int(input("Digite a quantidade de maças compradas: "))

if (macas_comparadas < 12):
    custo_total = macas_comparadas * 1.30
else:
    custo_total = macas_comparadas * 1.00

print(f"Custo do total da compra das maças é R${custo_total:.2f}")