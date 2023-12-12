#Calculadora de Soma
def soma(n1,n2):
    soma = n1 + n2
    return soma

#Calculadora de Subtração
def sub(n1,n2):
    sub = n1 + n2
    return sub

#Calculadora de Multiplicação
def mult(n1,n2):
    mult = n1 * n2
    return mult

#Calculadora de Divisão
def div(n1,n2):
    if n2 != 0:
        div = n1/n2
    else:
        div = "Indeterminado!"
    return div