from tkinter import *

box = Tk()
box.title("Exercício Soma 2 Valores.")
box.geometry("150x150")

def soma():
    sum = float(n1.get()) + float(n2.get())
    resp.configure(text=f"O Resultado da Soma é: {sum}")
    
n1_label = Label(text="Digite um valor:").pack()
n1 = Entry()
n1.pack()

n2_label = Label(text="Digite outro valor:").pack()
n2 = Entry()
n2.pack()

sum_button = Button(box,text="Somar",command=soma)
sum_button.pack()

resp = Label(text="")
resp.pack()

box.mainloop()