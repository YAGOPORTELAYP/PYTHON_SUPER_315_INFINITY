def o_maior(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return f"{n1} é o Maior!"
    elif n2 > n1 and n2 > n3:
        return f"{n2} é o Maior!"
    elif n3 > n1 and n3 > n2:
        return f"{n3} é o Maior!"
    else:
        return "Há mais de 1 maior do mesmo valor!"
    
maior = int(input("Digite 3 números:"))
print(o_maior(maior))