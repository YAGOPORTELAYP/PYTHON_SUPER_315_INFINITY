class Carro:
    def __init__(self,ano:int,marca:str,modelo:str,cor:str,qtde_portas:int,arcondicionado:bool,vidro_eletrico:bool):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.qtde_portas = qtde_portas
        self.arcondicionado = arcondicionado
        self.vidro_eletrico = vidro_eletrico

carro1=Carro(2022,"fiat","mobi","branco",4,True,True)
carro2=Carro(2007,"ford","fiesta","preto",4,True,True)
carro3=Carro(2009,"fiat","siena","preto",4,True,True)

print(carro1.marca,carro1.modelo)
print(carro2.modelo,carro2.ano,carro2.vidro_eletrico)
print(carro3.ano,carro3.marca,carro3.modelo,carro3.cor,carro3.qtde_portas,carro3.arcondicionado,carro3.vidro_eletrico)
        