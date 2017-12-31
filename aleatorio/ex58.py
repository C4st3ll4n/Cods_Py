from random import randint as r
compiuter = r(0, 10)
c = 1
while True:
    chute = int(input("Chute: "))
    if chute == compiuter:
        print("Acertou Mizeravi")
        print("Acertou em: {} tentativas".format(c))
        break
    else:
        print("Erroooooooooouu")
        c = c + 1
        continue
