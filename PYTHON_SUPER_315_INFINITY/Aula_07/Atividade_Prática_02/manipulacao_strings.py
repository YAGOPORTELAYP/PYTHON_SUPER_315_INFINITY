# Inverter a ordem das Palavras da string
def inverter(text):
    return text[::-1] 

# #Contar o número de palavras da string
def w_count(text):
    cont = 1
    for i in text.strip():
        if i == " ":
            cont += 1
    return cont
# Dizer se a string é um palíndromo ou não
def palindromo(text):
    text = text.replace(" ","")
    if text == inverter(text):
        return "É Palíndromo."
    else:
        return "Não é Palíndromo."