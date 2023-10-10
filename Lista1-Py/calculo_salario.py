#Escreva um programa para ler o salário bruto e o valor das horas extras trabalhadas

salb = int(input("Informe o salario bruto: "))
he = int(input("Informe o valor das horas extras trabalhadas: "))

salarioliquido = salb + he - (salb * 0.08)

print("Seu salario liquido é: ", salarioliquido)