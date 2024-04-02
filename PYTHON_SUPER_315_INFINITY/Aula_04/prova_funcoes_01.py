#[PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas. 
#Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. 
#Também crie uma função chamada "verificar_situacao" que, com base na média calculada, 
#irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, 
#"Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.

lista_notas = []
lista_notas = input(float("Digite suas notas:"))

def calcular_media(lista_notas):
  sum = 0
  for i in lista_notas:
    sum += i
  media = sum / len(lista_notas)

  return media

def verificar_situacao(media):
  if media < 7:
    print("Reprovado")
  elif media >= 7:
    print("Aprovado")
  elif media == 10:
    print("Parabéns, sua média é 10")
