lista = ["UVA", "PÊRA", "MELÃO", "MAÇA", "BANANA", "ACEROLA", "ABACAXI"]
while True:
    print(lista)
    excluir = int(input("""\nDigite o número relativo ao que você quer fazer na lista:
1 - Excluir o Último.
2 - Excluir pela posição.
0 - Sair.\n """))
    if excluir == 1:
        lista.pop()
        if len(lista) == 0:
            print("A lista está vazia!!!")
            break
    elif excluir == 2:
        print(lista)
        position = int(input("Digite a posição da fruta que você quer excluir:"))
        lista.pop(position - 1)
        if len(lista) == 0:
            print("A lista está vazia!!!")
            break 
    elif excluir == 0:
        break
    else:
        print("Posição Inválida!")

print(f"""A lista Ficou assim:\n
{lista}""")