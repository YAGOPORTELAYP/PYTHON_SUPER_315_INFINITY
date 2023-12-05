def vog(word:str):
    count = 0
    for i in word:
        if i in "aeiou":
            count += 1
    if count > 3:
        return "Mais de 3 Vogais!"
    elif count < 3:
        return "Menos de 3 Vogais!"
    else:
        return "São exatamente 3 Vogais!"
word = str(input("Digite uma palavra:")).lower()
print(vog(word))