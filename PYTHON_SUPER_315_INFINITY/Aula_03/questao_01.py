dicionario = {
"nome": "João", 
"idade": 13, 
"cpf": "000.000.000-00"}

if dicionario["idade"] > 18:
    dicionario["habilitacao"] = True
    print(dicionario)

else:
    dicionario["nome"] = "Joãozinho"
    print(dicionario)