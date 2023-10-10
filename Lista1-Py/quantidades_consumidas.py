#Escreva um programa para ler as quantidades consumidas por um cliente em cada produto

choc = int(input("Quantos chocolates foram consumidos? "))
refri = int(input("Quantos refrigerantes foram consumidos? "))
mist = int(input("Quantos Mistos Quentes foram consumidos? "))
sorv = int(input("Quantos sorvetes foram consumidos? "))

vchoc = choc * 1.50
vrefri = refri * 2.00
vmist = mist * 2.00
vsorv = sorv * 1.50

venda = vchoc + vrefri + vmist + vsorv

print("Sua conta é no valor de: ", venda, "R$")
