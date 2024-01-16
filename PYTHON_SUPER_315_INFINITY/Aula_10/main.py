from tkinter import *

box = Tk()
box.title("Qual número é o Maior?")
box.geometry("300x300")

def qualeMaior():
    
    num1 = float(n1.get())
    num2 = float(n2.get())

    if num1 > num2:
        ma = num1
        resp.configure(text=f"O maior número é: {ma}")
    elif num2 > num1:
        ma = num2
        resp.configure(text=f"O maior número é: {ma}")
    else:
        resp.configure(text=f"São iguais")

n1_label = Label(text="Digite o primeiro número:").pack()
n1 = Entry()
n1.pack()

n2_label = Label(text="Digite o segundo número:").pack()
n2 = Entry()
n2.pack()

maior_button = Button(box,text="O maior é...",command=qualeMaior)
maior_button.pack()

resp = Label(text="")
resp.pack()

box.mainloop()