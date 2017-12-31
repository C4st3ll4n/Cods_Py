n = int(input("Digite um número: "))
c = n
f = 1
print("Calculando {}!".format(n))
while c > 0:
    print("{}".format(c), end="")
    print(" * " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f)
print("THE END")