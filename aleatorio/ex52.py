p = int(input("Quantas vezes deseja fazer o teste dos primos ?\nResposta:  "))
for c in range(p):
    a = int(input("\nDigite um número: "))
    t = a / a
    z = a / 1
    if t == 1 and z == a:
        if a % 2 != 0:
            print("BINGO, {} é um número primo !\n".format(a))
        else:print("Ops, de acordo com os cálculos {} não é um número primo\n".format(a))
