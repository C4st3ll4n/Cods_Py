pri = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, " ", end="")
        termo = termo + razao
        cont += 1
    print("\nWait for it....")
    decisao = input("Deseja mostrar algum número a mais ?\n[S/N] ")
    if decisao == "S":
        mais = int(input("Quantos ? "))
    else:
        print("Total de termos: {}".format(total))
        break
print("Fim!")

