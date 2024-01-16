from tkinter import*

caixa = Tk()
caixa.title("Semáforo")
caixa.geometry("200x300")

def red():
    resp.configure(text="PARE")
def ye():
    resp.configure(text="ATENÇÃO")
def gr():
    resp.configure(text="SIGA")

pare_button=Button(width=7, height=3,bg="red",command=red).pack()
atencao_button=Button(width=7, height=3,bg="yellow",command=ye).pack()
siga_button=Button(width=7, height=3,bg="green",command=gr).pack()

resp=Label(text="")
resp.pack()

caixa.mainloop()