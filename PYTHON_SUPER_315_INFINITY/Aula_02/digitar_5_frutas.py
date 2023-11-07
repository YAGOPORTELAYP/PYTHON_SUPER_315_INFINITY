lista_F = ["UVA","PÊRA","MELÃO"]
while True:
    frutas = str(input(f"Digite o nome de uma fruta que você quer adicionar a lista:"))
    lista_F.append(frutas)
    add_frutas = str(input("Você quer adicionar mais uma fruta? ( S --> SIM | N --> NÃO)")).lower()
    if add_frutas == "s":
        continue
    else:
        break
print(lista_F)