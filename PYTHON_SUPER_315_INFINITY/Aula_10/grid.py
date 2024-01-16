from tkinter import*

janela=Tk()
janela.title("Aprendendo GRID")
janela.geometry("300x300")

idade_label=Label(text="Digite sua idade:")
idade_label.grid(row=0,column=0)

idade_imput=Entry()
idade_imput.grid(row=0,column=1)

altura_Label=Label(text="Digite sua altura:")
altura_Label.grid(row=1,column=0)

altura_imput=Entry()
altura_imput.grid(row=1,column=1)

botao=Button(text="Enviar",width=30)
botao.grid(row=2,column=0,columnspan=2)

janela.mainloop()