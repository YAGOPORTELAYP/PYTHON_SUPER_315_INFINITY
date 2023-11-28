num = int(input("Digite um Número:"))
mqdez = lambda num: num if num > 10 else (num/2)
print(mqdez(num))