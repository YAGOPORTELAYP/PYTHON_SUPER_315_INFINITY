import random
from random import choice
usuario = str(input("Digite p, f ou t para pedra, papel ou tesoura:")).lower()
lista_jokempo = ["p","f","t"]
machine = random.choice(lista_jokempo)
def jokempo(usuario=str,machine=str):
    if (usuario == lista_jokempo[0] or usuario == lista_jokempo[2] or usuario == lista_jokempo[1]) and (machine == lista_jokempo[0] or machine == lista_jokempo[2]):
        return "Você ganhou!"
    elif (machine == lista_jokempo[0] or machine == lista_jokempo[2] or machine == lista_jokempo[1]) and (usuario == lista_jokempo[0] or usuario == lista_jokempo[2]):
        return "A Máquina ganhou!"
    elif machine == usuario:
        return "Empate!"
print(jokempo(usuario,machine))