# Contador de Caracteres
def qnt_char(palavra):
    return len(palavra)

# Contador de Vogais
def qnt_vogais(palavra):
    vog = 0
    for i in palavra:
        if i in "aáâãàeéèêiíìîoóòõôuúùû":
            vog += 1
    return vog

# Contador de Consoantes
def qnt_consoantes(palavra):
    cons = 0
    for i in palavra:
        if i not in "bcdfghjklmnpqrstuvwxyz":
            cons += 1
    return cons

# Contador de Espaços Vazios
def qnt_vazios(palavra):
    vazio = 0
    for i in palavra:
        if i in " ":
            vazio += 1
    return vazio