pri = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = pri
cont = 1
while cont <= 10:
    print(termo, " ", end="")
    termo = termo + razao
    cont += 1
print("Acabou !")

