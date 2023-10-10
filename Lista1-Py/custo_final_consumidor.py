"""Escrever um programa para ler o custo de fabrica de um carro, e exibir o custo final ao consumidor
que é calculado como sendo : custo de fabrica + porcentagem do distribuidor + porcentagem dos impostos,
sabendo que o percentual do distribuidor é de 28% do custo de fabrica e os impostos correspondentes 
a 45% do custo de fabrica."""

custofabri = int(input("Qual o custo de fabrica? "))

dist = custofabri * 0.28
impost = custofabri * 0.45

custofinalconsum = custofabri + dist + impost 

print("O custo final para o consumidor é ", custofinalconsum)

