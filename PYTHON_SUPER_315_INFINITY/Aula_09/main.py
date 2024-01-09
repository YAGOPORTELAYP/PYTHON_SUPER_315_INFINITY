from tkinter import *

caixinha = Tk()
caixinha.title("Aula 1 TK")
caixinha.geometry("300x300")

def saudacao():
    nome = usuario_imput.get()
    result.configure(text=f"Bem Vindo {nome}!")

usuario_label = Label(text="Digite o seu nome de usuário:")
usuario_label.pack()

usuario_imput = Entry()
usuario_imput.pack()

usuario_botao = Button(caixinha,text = "Salvar", command = saudacao,background="green",fg="white",font=("Calibri",18,"bold"))
usuario_botao.pack()

result = Label(text="") 
result.pack()

caixinha.mainloop()