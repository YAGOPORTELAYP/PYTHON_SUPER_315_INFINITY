from tkinter import*

box = Tk()
box.title("Salário do Usuário")
box.geometry("300x300")

def sal_hora():
    hora = float(hora_trab.get())
    calc = float(sal_mensal.get())/hora
    if hora_trab != 0 and hora_trab <= 10:
        resposta.configure(text=f"Ele ganha {calc} reais por hora.",bg=red,fg=white)
    elif hora_trab >= 11 and hora_trab <= 25:
        resposta.configure(text=f"Ele ganha {calc} reais por hora.",bg=orange,fg=white)
    elif hora_trab >= 26 and hora_trab <= 50:
        resposta.configure(text=f"Ele ganha {calc} reais por hora.",bg=blue,fg=white)
    elif hora_trab >= 51:
        resposta.configure(text=f"Ele ganha {calc} reais por hora.",bg=pink,fg=white)

sal_label = Label(text="Digite o seu salário mensal:").pack()
sal_mensal = Entry()
sal_mensal.pack()

hora_label = Label(text="Digite as suas horas de trabalho mensais:").pack()
hora_trab = Entry()
hora_trab.pack()

maior_button = Button(box,text="Salário",command=sal_hora)
maior_button.pack()

resposta = Label(text="")
resposta.pack()

box.mainloop()