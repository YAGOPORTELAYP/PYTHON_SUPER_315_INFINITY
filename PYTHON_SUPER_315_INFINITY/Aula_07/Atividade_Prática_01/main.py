while True:
    print("Menu da Calculadora")
    print("Digite A para Adição.")
    print("Digite S para Subtração.")
    print("Digite M para Multiplicação.")
    print("Digite D para Divisão.")

    menu = str(input()).upper()
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))

    while True:
        if menu == "A":
            from calculadora import soma
            print(f"O Resultado da Soma é:  {soma(n1=n1,n2=n2)}")
            break
        elif menu == "S":
            from calculadora import sub
            print(f"O Resultado da Subtração é:  {sub(n1=n1,n2=n2)}")
            break
        elif menu == "M":
            from calculadora import mult
            print(f"O Resultado da Multiplicação é:  {mult(n1=n1,n2=n2)}")
            break
        elif menu == "D":
            from calculadora import div
            print(f"O Resultado da Divisão é:  {div(n1=n1,n2=n2)}")
            break
        else:
            print("Operação Inválida! Digite A,S,M OU D.")
            continue

    tsuzuku = int(input("""Você deseja fazer mais alguma operação?
                        Digite 1 para Sim.
                        Digite 2 para Não.
                        """))
    if tsuzuku == 1:
        continue
    elif tsuzuku == 2:
        print("Até Mais!!")
        break