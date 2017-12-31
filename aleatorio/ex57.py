while True:
    print("Digite seu sexo [(F)eminino/(M)asculino/(I)ndefinido]")
    sexo = input("Resposta: ")
    if sexo.upper() == "M" or sexo.upper() == "F" or sexo.upper() == "I":
        print("! --FIM-- !")
        break
    else: print("\nUATAFOQUI ?\n")