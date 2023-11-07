excluir = int(input("Digite o número da posição da fruta que você quer excluir:"))
lista = ["UVA", "PÊRA", "MELÃO", "MAÇA", "BANANA", "ACEROLA", "ABACAXI"]
lista.pop(excluir-1)
print(lista)