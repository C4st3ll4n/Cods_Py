from random import randint as rr
v = 0
d = 0
while True:
    jogador = int(input("Digite um valor: "))
    pc = rr(0,11)
    t = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = input("Par ou Impar? [P/I]\n ").strip().upper()[0]
    print(f'Deu {t}')
    if tipo == "P":
        if t % 2 == 0:
            print("YOU WIN !")
            v += 1
        else:
            print("YOU LOOOOSE !")
            d += 1
    if tipo == "I":
        if t % 2 == 1:
            v += 1
            print("YOU WIN !")
        else:
            print("YOU LOOOOSE !")
            d += 1
    print("Eae, vamos de novo ?!")
    resposta = input("[S/N]")
    if resposta.strip().upper()[0] == "S":
        continue
    else:
        print(f"Vitórias = {v}\nDerrotas = {d}")
        print("Tchau Tchau !")
        break
print("\nFIM !")