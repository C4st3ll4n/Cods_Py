inp("Números ímpares e múltiplos de três: ")
for c in range(1, 501):
    m = c % 3
    i = c % 2
    if m == 0 and i == 1: print(c)
