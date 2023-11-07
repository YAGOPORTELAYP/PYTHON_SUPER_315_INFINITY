prod = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
total = 0
for x in prod:
    print("\n",x)
    total = (prod[0][1])+(prod[1][1])+(prod[2][1])
print(f"\nO valor total dos produtos é: {total}\n")