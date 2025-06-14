import tkinter 
m = tkinter.Tk()
w = tkinter.Label(m, text='CADASTRO DO ALUNO') #criação de um rótulo no centro da pagina 
w.pack() #add e dimensiona 
frame = tkinter.Frame(m) #area retangular
frame.pack (padx=10, pady=15) # pack visualizar e pad - > espaçamento
tkinter.Label(frame, text='Nome completo: ').grid(row=0, column=0)
e1 = tkinter.Entry(frame)
e1.grid(row=0, column=1)

tkinter.Label(frame, text='Matrícula: ').grid(row=1, column=0)
e2 = tkinter.Entry(frame)
e2.grid(row=1, column=1)
m.title('Cadastrar')
button = tkinter.Button(m, text='Cadastrar', width=25, command=m.destroy)
button.pack() #add widget #escri algo aqui
m.mainloop()






