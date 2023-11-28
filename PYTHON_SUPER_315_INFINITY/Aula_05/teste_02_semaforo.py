def semaforo(saida:str):
    if saida == "VERDE":
        return "CONTINUE!"
    elif saida == "AMARELO":
        return "ATENÇÃO!"
    elif saida == "VERMELHO":
        return "PARE!"
    else:
        return "ERROR!"

while True:
    saida = str(input("Digite uma cor:")).upper()
    resp = semaforo(saida)

    if resp != "ERROR!":
        print(resp)
        break
    else:
        print(resp)