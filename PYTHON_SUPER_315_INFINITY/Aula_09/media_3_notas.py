from tkinter import *

box = Tk()
box.title("Calcular Média")
box.geometry("300x300")

def media():
    med = (float(n1.get()) + float(n2.get()) + float(n3.get()))/3
    if med >= 7 and med < 10:
        resp.configure(text=(f"Você foi aprovado"),bg="green",fg="white")
    elif med < 7 and med >= 0:
        resp.configure(text=(f"Você foi Reprovado"),bg="red",fg="white")
    elif med == 10:
        resp.configure(text=(f"Aprovado com distinção"),bg="blue",fg="white")
    else:
        resp.configure(text=(f"Nota {med} é Inválida"),bg="gray",fg="white")

n1_label = Label(text="Digite a primeira nota:").pack()
n1 = Entry()
n1.pack()

n2_label = Label(text="Digite a segunda nota:").pack()
n2 = Entry()
n2.pack()

n3_label = Label(text="Digite a terceira nota:").pack()
n3 = Entry()
n3.pack()

media_botao = Button(text="Calcular a Média",command=media)
media_botao.pack()

resp = Label(text="")
resp.pack()

box.mainloop()