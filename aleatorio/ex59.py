print("[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair\n")
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

while True:
    opção = int(input("Opção: "))
    if opção == 1:
        print("Resultado = {}".format(n1+n2))
    if opção == 2:
        print("Resultado = {}".format(n1 * n2))
    if opção == 3:
        if n1 > n2:
            print("Maior é o 1º número = {}".format(n1))
        else:
            print("Maior é o 2º número = {}".format(n2))
    if opção == 4:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    if opção == 5:
        print("! ## Tchau ## !")
        break
