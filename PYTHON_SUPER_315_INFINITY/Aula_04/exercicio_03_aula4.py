def saudacao(nome:str, hora:int):
  if hora >= 5 and hora <= 12:
    return f"bom dia {nome}"
  elif hora > 12 and hora <= 18:
    return f"boa tarde {nome}"
  else:
    return f"boa noite {nome}"
  
name = str(input("Digite seu nome: "))
hr = int(input("Digite a hora:"))

print(saudacao(hora=hr, nome=name))