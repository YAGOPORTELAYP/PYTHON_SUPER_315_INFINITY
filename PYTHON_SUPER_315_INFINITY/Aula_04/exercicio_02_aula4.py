def o_maior(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return f"O número {n1} é o Maior!"
    elif n2 > n1 and n2 > n3:
        return f"O número {n2} é o Maior!"
    elif n3 > n1 and n3 > n2:
        return f"O número {n3} é o Maior!"
    else:
        return "Há mais de 1 maior do mesmo valor!"
lista = [] 
for i in range(1,4):
    maior = int(input(f"Digite o {i}º número:"))
    list.append(maior)

print(o_maior(list[0],list[1],list[2]))