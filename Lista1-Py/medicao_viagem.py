#Escreva um programa para  medir a distancia percorrida , o tempo gasto na viagem, a velocida de media e o consumo em litros do veiculo

kml = float(input("Quantos KM o carro faz com 1 litro de gasolina? "))
temp = float(input("Tempo gasto na viagem em minutos "))
vel = float(input("Qual a velocidade media da viagem em KM por hora? "))

distancia = (vel * temp)/60
litroscombustivel = distancia / kml

print("A distancia percorrida foi de ", distancia, "KM e a autonomia do carro foi de ", litroscombustivel, "Litros de combustivel.")

