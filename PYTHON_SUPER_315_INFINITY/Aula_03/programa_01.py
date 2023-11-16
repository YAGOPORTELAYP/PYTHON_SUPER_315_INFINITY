# Leia os dados de um usuário - nome, sobrenome, idade, email - e
# imprima-os enumerando os mesmos.
# Leia 4 notas de um aluno, calcule sua média e armazene em um
# dicionário as seguintes informações:
# a. Nome do aluno
# b. As 4 notas obtidas
# c. Maior nota
# d. Menor nota
# e. Média
# f. Situação
# Agora imprima as informações deste aluno na saída padrão
usuario = {"1-nome": "Yago","2-sobrenome":"Portela","3-idade":"23 Anos","4-email":"theypsv@gmail.com"}
print(usuario)
nt = "Nota "
notas = []



for i in range(1,5):
    
    valores = float(input(f"Digite a {i}ª Nota:"))
    notas.append(valores)
    nota = {nt+str(i):notas }

print(notas) 