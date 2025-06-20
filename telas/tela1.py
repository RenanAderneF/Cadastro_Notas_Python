import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
import sys
sys.path.insert(0, './db')
from db import cadastraAluno, getAlunos, addDisciplina, getDisciplinas, addAvaliacao, getAvaliacoes

# Variáveis:
colors = {
    'principal': '#ebeac4',
    'secundaria': '#156382',
    'terciaria': '#0c3444',
    'campos': '#f8fae4',
    'textoCabecalhos': "#ffffff",
    'fundoCabecalhos': '#bd8c75',
}

fonts = {
    'cabecalho1': ('Helvetica', 18),
    'cabecalho2': ('Helvetica', 12)
}

larguraTela = 1000
alturaTela = 800

# Página inicial:

class meuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de notas")
        self.geometry("900x800")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for i in (telaAlunos, telaDisciplinas, telaAvaliacoes):
            nome = i.__name__
            frame = i(container, self)
            self.frames[nome] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self._criaMenu()
        self.mostraPagina("telaAlunos")

    def _criaMenu(self):
        menuBar = tk.Menu(self)
        menuPaginas = tk.Menu(menuBar, tearoff=0)
        menuPaginas.add_command(label="Alunos", command=lambda: self.mostraPagina("telaAlunos"))
        menuPaginas.add_command(label="Disciplinas", command=lambda: self.mostraPagina("telaDisciplinas"))
        menuPaginas.add_command(label="Avaliações", command=lambda: self.mostraPagina("telaAvaliacoes"))
        menuBar.add_cascade(label="Páginas", menu=menuPaginas)
        self.config(menu=menuBar)

    def mostraPagina(self, nome_pagina):
        frame = self.frames[nome_pagina]
        frame.tkraise()
        
# Telas navegáveis:
class telaAlunos(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Widgets:

        # FrameCadastro:
        frameCadastro = tk.Frame(self, width=larguraTela/3, height=alturaTela, bg= colors['principal'], padx=10)

        labelCadastro = tk.Label(self, text='Alunos', anchor="w", foreground=colors['textoCabecalhos'], bg= colors['secundaria'], font=fonts['cabecalho1'])

        labelAluno = tk.Label(frameCadastro, text='Registrar e visualizar alunos', foreground=colors['textoCabecalhos'], bg= colors['terciaria'], font=fonts['cabecalho2'])

        labelNome = tk.Label(frameCadastro, text="Nome Completo:", width=20, anchor='w', background= colors['principal'])

        entryNome = tk.Entry(frameCadastro)

        labelMatricula = ttk.Label(frameCadastro, text="Matrícula:", width=20, anchor='w', background= colors['principal'])

        entryMatricula = ttk.Entry(frameCadastro)

        # Botão de cadastro de aluno:
        btnEnviar = tk.Button(frameCadastro, text="Enviar")

        # Recebe dados inseridos nos campos de entrada, e os utiliza de argumento para função 'geraTabela()':
        def enviaCadastro():
            try:
                nome= entryNome.get()
                matricula= entryMatricula.get()

                if not nome or not matricula:
                    messagebox.showinfo("Preenchimento incorreto", "Preencha todos os dados.")
                    return
                
                if len(matricula) < 12 or len(matricula) > 12:
                    messagebox.showinfo("Preenchimento incorreto", "A matrícula deve conter 12 caracteres.")
                    return
                
                cadastraAluno(nome, matricula)
                carregaTabela()

            except():
                messagebox.showinfo("Conflito", 'Unicidade de dados não respeitada. Nome ou matrícula já registrados no banco.')

        btnEnviar.config(command=lambda: enviaCadastro())

        # FrameVisualização:
        frameVisualizacao = tk.Frame(self, width=larguraTela/2, bg= colors['principal'], padx=10)

        # Tabela com scroll:
        scroll = ttk.Scrollbar(frameVisualizacao)
        table = ttk.Treeview(frameVisualizacao, yscrollcommand= scroll.set,columns = ('nome', 'matricula'), show = 'headings', height=100)
        table.heading('nome', text='Nome Completo')
        table.heading('matricula', text='Matrícula')
        scroll.config(command= table.yview)

        # Carrega dados atualizados na tabela, presentes no banco de dados:
        def carregaTabela():

            # Limpa tabela:
            for item in table.get_children():
                table.delete(item)

            # Adiciona dados atualizados:
            dados = getAlunos()

            for i in range(len(dados)):
                aluno = dados[i]
                table.insert(parent='', index = 0, values = aluno)

        # Pack:
        labelCadastro.pack(side='top', fill='both')
        frameCadastro.pack(side = 'left', fill='both')
        scroll.pack(side='right', fill='y')
        frameVisualizacao.pack(side = 'right', fill='both', expand=True)

        # Grid (FrameCadastro):
        labelAluno.grid(column=0, row=0, pady= 10)
        labelNome.grid(column=0, row=1, pady=5)
        entryNome.grid(column=1,row=1)
        labelMatricula.grid(column=0, row=2)
        entryMatricula.grid(column=1, row=2)
        btnEnviar.grid(column=1,row=3, pady=5)

        # Pack (FrameVisualização)
        table.pack(side = 'left', fill='both')

class telaDisciplinas(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Widgets:

        # FrameCadastro:
        frameCadastro = tk.Frame(self, width=larguraTela/2, height=alturaTela, bg= colors['principal'], padx=10)

        labelCadastro = tk.Label(self, text='Disciplinas', anchor="w", foreground=colors['textoCabecalhos'], bg= colors['secundaria'], font=fonts['cabecalho1'])

        labelAluno = tk.Label(frameCadastro, text='Registrar e visualizar alunos', foreground=colors['textoCabecalhos'], bg= colors['terciaria'], font=fonts['cabecalho2'])

        labelNome = tk.Label(frameCadastro, text="Nome da Disciplina", width=20, anchor='w', background= colors['principal'])
        entryNome = tk.Entry(frameCadastro)

        # Botão de cadastro de aluno:
        btnEnviar = tk.Button(frameCadastro, text="Enviar")

        # Recebe dados inseridos nos campos de entrada, e os utiliza de argumento para função 'geraTabela()':
        def enviaCadastro():
            try:
                nome= entryNome.get()

                if not nome:
                    messagebox.showinfo("Preenchimento incorreto", "Preencha o nome da disciplina.")
                    return
                
                addDisciplina(nome)
                carregaTabela()

            except():
                messagebox.showinfo("Conflito", 'Unicidade de dados não respeitada. Nome ou matrícula já registrados no banco.')

        btnEnviar.config(command=lambda: enviaCadastro())

        # FrameVisualização:
        frameVisualizacao = tk.Frame(self, width=larguraTela/2, bg= colors['principal'], padx=10)

        # Tabela com scroll:
        scroll = ttk.Scrollbar(frameVisualizacao)
        table = ttk.Treeview(frameVisualizacao, yscrollcommand= scroll.set,columns = ('nome',), show = 'headings', height=100)
        table.column('nome', width=300, anchor='center')
        table.heading('nome', text='Nome da Disciplina')
        scroll.config(command= table.yview)

        # Carrega dados atualizados na tabela, presentes no banco de dados:
        def carregaTabela():

            # Limpa tabela:
            for item in table.get_children():
                table.delete(item)

            # Adiciona dados atualizados:
            dados = getDisciplinas()

            for i in range(len(dados)):
                disciplina = dados[i]
                table.insert(parent='', index = 0, values = disciplina)

        # Pack:
        labelCadastro.pack(side='top', fill='both')
        frameCadastro.pack(side = 'left', fill='both')
        scroll.pack(side='right', fill='y')
        frameVisualizacao.pack(side = 'right', fill='both', expand=True)

        # Grid (FrameCadastro):
        labelAluno.grid(column=0, row=0, pady= 10)
        labelNome.grid(column=0, row=1, pady=5)
        entryNome.grid(column=1,row=1)
        btnEnviar.grid(column=1,row=3, pady=5)

        # Pack (FrameVisualização)
        table.pack(side="left", fill='both')

class telaAvaliacoes(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Widgets:

        # FrameCadastro:
        frameCadastro = tk.Frame(self, width=larguraTela/3, height=alturaTela, bg= colors['principal'], padx=10)

        labelCadastro = tk.Label(self, text='Avaliações', anchor="w", foreground=colors['textoCabecalhos'], bg= colors['secundaria'], font=fonts['cabecalho1'])

        labelAluno = tk.Label(frameCadastro, text='Registrar e visualizar avaliações', foreground=colors['textoCabecalhos'], bg= colors['terciaria'], font=fonts['cabecalho2'])

        labelNome = tk.Label(frameCadastro, text="Matrícula de aluno:", width=20, anchor='w', background= colors['principal'])
        entryNome = tk.Entry(frameCadastro)

        labelDisciplina = ttk.Label(frameCadastro, text="Disciplina:", width=20, anchor='w', background= colors['principal'])
        entryDisciplina = ttk.Entry(frameCadastro)

        labelNota1  = ttk.Label(frameCadastro, text="Nota da 1° avaliação", anchor="w", background= colors['principal'])
        entryNota1 = ttk.Entry(frameCadastro)
        labelNota2 = ttk.Label(frameCadastro, text="Nota da 2° avaliação",  width=20, anchor="w", background= colors['principal'])
        entryNota2 = ttk.Entry(frameCadastro)
        labelData = ttk.Label(frameCadastro, text="Data da avaliação",  width=20, anchor="w", background= colors['principal'])
        entryData = ttk.Entry(frameCadastro)

        # Botão de cadastro de aluno:
        btnEnviar = tk.Button(frameCadastro, text="Enviar")

        # Recebe dados inseridos nos campos de entrada, e os utiliza de argumento para função 'geraTabela()':
        def enviaCadastro():
           
            nome= entryNome.get()
            disciplina= entryDisciplina.get()
            nota1 = entryNota1.get()
            nota2 = entryNota2.get()
            data = entryData.get()

            addAvaliacao(nome, disciplina, nota1, nota2, data)
            carregaTabela()

           
        btnEnviar.config(command=lambda: enviaCadastro())

        # FrameVisualização:
        frameVisualizacao = tk.Frame(self, width=larguraTela/2, bg= colors['principal'], padx=10)

        # Tabela com scroll:
        scroll = ttk.Scrollbar(frameVisualizacao)
        table = ttk.Treeview(frameVisualizacao, yscrollcommand= scroll.set,columns = ('nome', 'disciplina', 'nota1', 'nota2', 'data'), show = 'headings', height=100)
        table.column('nome', width=120, anchor="center")
        table.column('disciplina', width=120, anchor="center")
        table.column('nota1', width=120, anchor="center")
        table.column('nota2', width=120, anchor="center")
        table.column('data', width=120, anchor="center")
        table.heading('nome', text='Nome Completo')
        table.heading('disciplina', text='Disciplina')
        table.heading('nota1', text='1° nota')
        table.heading('nota2', text='2° nota')
        table.heading('data', text='Data')
        scroll.config(command= table.yview)

        # Carrega dados atualizados na tabela, presentes no banco de dados:
        def carregaTabela():

            # Limpa tabela:
            for item in table.get_children():
                table.delete(item)

            # Adiciona dados atualizados:
            dados = getAvaliacoes()

            for i in range(len(dados)):
                aluno = dados[i]
                table.insert(parent='', index = 0, values = aluno)


        # Pack:
        labelCadastro.pack(side='top', fill='both')
        frameCadastro.pack(side = 'left', fill='both')
        scroll.pack(side='right', fill='y')
        frameVisualizacao.pack(side = 'right', fill='x')

        # Grid (FrameCadastro):
        labelAluno.grid(column=0, row=0, pady= 10)
        labelNome.grid(column=0, row=1, pady=5)
        entryNome.grid(column=1,row=1)
        labelDisciplina.grid(column=0, row=2, pady=5)
        entryDisciplina.grid(column=1, row=2)
        labelNota1.grid(column=0, row=3, pady=5)
        entryNota1.grid(column=1, row=3)
        labelNota2.grid(column=0, row=4, pady=5)
        entryNota2.grid(column=1, row=4)
        labelData.grid(column=0, row=5, pady=5)
        entryData.grid(column=1, row=5)
        btnEnviar.grid(column=1,row=6, pady=5)

        # Pack (FrameVisualização)
        table.pack(fill='both')

if __name__ == "__main__":
    app = meuApp()
    app.mainloop()


    