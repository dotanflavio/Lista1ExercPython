"""faça um programa que leia o numero vendido de carros e o valor das vendas totais do vendedor.
em seguida , Calcule  e exiba o salario final do vendedor sabendo que a empresa paga um salario fixo
de R$622,00 mais um comissao de R$30,00 por cada carro vendido, mais 5% do valor total de vendas
do vendedor."""

carros = int(input("Quantos carros foram vendidos? "))
valortotalvendas = int(input("Qual o valor total de suas vendas? "))

salariofixo = 622.00
comissao = carros * 30.00
porctotalvendas = valortotalvendas * 0.05

salariofinal = salariofixo + comissao + porctotalvendas

print("Seu salario final é ", salariofinal)