words = ["Python", "é", "uma", "linguagem", "poderosa"]
palavras = []
for x in words:
    if len(x) > 4:
        palavras.append(x)
print(f"As palavras que possuem mais de 4 dígitos são: {palavras}")