num = int(input("Digite um Número:"))
div = lambda num: "Divisível!" if num % 3 ==0 and num % 5 == 0 else "Não Divisível!"
print(div(num))