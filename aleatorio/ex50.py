r = int()
for c in range(0, 6):
    a = int(input("Digite um número: "))
    b = a % 2
    if b == 0:
        r = r + a
    else: pass
print(r)