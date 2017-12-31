print("Sequencia de Fibs")
t1 = 0
t2 = 1
n = int(input("Quantos termos quer ver?\n"))
c = 3
print("{} → {}".format(t1, t2), end='')
while c<=n:
    t3 = t1 + t2
    print(" → {}".format(t3), end='')
    c +=1
    t1 = t2
    t2 = t3
print("FIM")
