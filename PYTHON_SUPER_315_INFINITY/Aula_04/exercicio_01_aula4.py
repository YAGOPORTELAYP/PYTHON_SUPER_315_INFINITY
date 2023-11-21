def Horario(hor):
    if hor >= 6 and hor < 13:
        return "Bom Dia!"
    elif hor >= 13 and hor < 18:
        return "Boa Tarde!"
    else:
        return "Boa Noite!"
    
hor = int(print("Digite que horas são:"))
print(Horario(hor))