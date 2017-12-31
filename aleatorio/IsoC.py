import serial

porta = 'COM11'
baud_rate = 9600
Obj_porta = serial.Serial(porta, baud_rate)
print("[1] Ligar LED\n[2]Desligar\n[3]LOOP\n")


def escrever_porta():
    try:
        v = int(input("\n1, 2 ou 3 ?\n"))
        valor = bytes([v])
        Obj_porta.write(valor)
        ler_porta(Obj_porta)

    except serial.SerialException:
        print("ERRO: Verifique se ha algum dispositivo conectado na porta!")


def ler_porta(Obj_porta):
    letra = Obj_porta.read_until('!', 9)
    print(letra, "\n")


if __name__ == '__main__':
    while True:
        escrever_porta()
