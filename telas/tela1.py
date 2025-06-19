import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
import sys
sys.path.insert(0, './db')
from db import cadastraAluno, getAlunos

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

nomes= ('Ana Beatriz Silva', 'Carlos Eduardo Santos', 'Mariana Oliveira Costa')
matriculas=("2019124831","2021057394", "2023031957")
larguraTela = 900
alturaTela = 800

# Tela de alunos:
class telaAlunos:
    def __init__(self):

        # Janela:
        self.root = tk.Tk()
        self.root.title("Layout intro")
        self.root.geometry(f"{larguraTela}x{alturaTela}")
        
        # Widgets:

        # FrameCadastro:
        frameCadastro = tk.Frame(self.root, width=larguraTela/3, height=alturaTela, bg= colors['principal'], padx=10)

        labelCadastro = tk.Label(self.root, text='Alunos', anchor="w", foreground=colors['textoCabecalhos'], bg= colors['secundaria'], font=fonts['cabecalho1'])

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
        frameVisualizacao = tk.Frame(self.root, width=larguraTela/2, bg= colors['principal'], padx=10)

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
        frameCadastro.pack(side = 'left', fill='both', expand=True)
        scroll.pack(side='right', fill='y')
        frameVisualizacao.pack(side = 'right', fill='x')

        # Grid (FrameCadastro):
        labelAluno.grid(column=0, row=0, pady= 10)
        labelNome.grid(column=0, row=1, pady=5)
        entryNome.grid(column=1,row=1)
        labelMatricula.grid(column=0, row=2)
        entryMatricula.grid(column=1, row=2)
        btnEnviar.grid(column=1,row=3, pady=5)

        # Pack (FrameVisualização)
        table.pack(fill='both')

        # Executar:
        self.root.mainloop()



telaAlunos()

    