from Contadores import *
palavra = str(input("Digite uma palavra ou frase:"))

print(f"Há {qnt_char(palavra=palavra)} Caracteres.")
print(f"Há {qnt_vogais(palavra=palavra)} Vogais.")
print(f"Há {qnt_consoantes(palavra=palavra)} Consoantes.")
print(f"Há {qnt_vazios(palavra=palavra)} Epaços Vazios.")