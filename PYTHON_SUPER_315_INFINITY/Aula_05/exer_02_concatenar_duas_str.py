w1 = str(input("Digite uma palavra:"))
w2 = str(input("Digite outra palavra:"))
conc = lambda w1, w2 : w1 + w2 if len(w1) > 5 and len(w2) > 5 else "Erro!"
print(conc(w1,w2))