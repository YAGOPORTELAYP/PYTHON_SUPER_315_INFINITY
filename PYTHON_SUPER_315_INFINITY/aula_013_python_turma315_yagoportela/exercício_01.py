class Dispositivo:
    def __init__(self,marca:str,modelo:str,cor:str) -> None:
        self.marca=marca
        self.modelo=modelo
        self.cor=cor
        self.ligado=False

    def ligar(self):
        if self.ligado:
            self.ligado = True
            return f"{self.modelo} ligou!"
        else:
            return "O aparelho já se encontra ligado!"
    
    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            return f"{self.modelo} desligou!"
        else:
            return "O aparelho já se encontra desligado!"
