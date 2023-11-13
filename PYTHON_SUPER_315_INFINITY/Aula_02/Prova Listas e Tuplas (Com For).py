lista = []
list_par = []
par_count = 0
sum_par = 0
list_impar = []
impar_count= 0
sum_impar = 0
print("Digite 10 Números:")
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º Número:"))
    lista.append(valor)

    if valor % 2 == 0:
        list_par.append(valor)
        par_count += 1
        sum_par += valor

    elif valor % 2 == 1:
        list_impar.append(valor)
        impar_count += 1
        sum_impar += valor

print(f"A Tupla de números pares é:",tuple(list_par))
print(f"A Tupla de números ímpares é:",tuple(list_impar))
print(f"""A quantidade de números pares e ímpares presentes na lista:\n
Números pares: {par_count}.
Números ímpares: {impar_count}.
Soma dos pares: {sum_par}.
Soma dos Ímpares: {sum_impar}.""")
        