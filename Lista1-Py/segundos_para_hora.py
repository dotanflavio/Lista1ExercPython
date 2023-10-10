#Faça um programa para converter segundos em formato de hora padrão

seg = int(input("Digite os segundos voce deseja converter "))

hr = int(seg / 3600)
mnt = int((seg - (hr * 3600))/60)
segr = int(seg % 60)

print(seg, "No formato de Horas padrao é ", hr,":",mnt,":",segr)