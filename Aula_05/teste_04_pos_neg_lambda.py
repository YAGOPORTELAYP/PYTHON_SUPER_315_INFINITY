pos_neg = lambda num: "Positivo" if num > 0 else "Negativo" if num < 0 else "Neutro"
num = int(input("Digite um Número:"))
print(pos_neg(num))