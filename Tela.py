from mailbox import mboxMessage
from operator import iconcat
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tokenize import String
import sqlite3
root = Tk()
bg = PhotoImage('./imagemEmpresa.jpg')

class Funcs():
    def limpa_tela(self):
        res = mb.askquestion('Limpar Dados','Deseja relamente limpar os dados?')
        if (res=='yes'):        
            self.inp_codigo.delete(0,END)
            self.inp_nomeAluno.delete(0,END)
            self.inp_instrutor.delete(0,END)
    def limpa_telaSemPergunta(self):
            self.inp_codigo.delete(0,END)
            self.inp_nomeAluno.delete(0,END)
            self.inp_instrutor.delete(0,END)    
    # def salvarDados(self):
    #     codigo = self.inp_codigo
    #     if(codigo.get() == ''):
    #             mb.showinfo('Aviso','Preencha todos os campos!')
    #             self.inp_codigo.focus()
    def conectaDB(self):
        self.conn = sqlite3.connect('certificados.db')
        self.cursor = self.conn.cursor()
    def desconectaDB(self):
        self.conn.close()
    def montaTabela(self):
        self.conectaDB()
        #criando tabela 
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS certificados(
            cod INTERGER PRIMARY KEY,
            nome_aluno CHAR(40) NOT NULL,
            nome_treinador CHAR(40) NOT NULL
        )""")
        self.conn.commit()
        self.desconectaDB()
    def addCertificado(self):
        self.codigo = self.inp_codigo.get()
        self.aluno = self.inp_nomeAluno.get()
        self.instrutor = self.inp_instrutor.get()
        
        self.conectaDB()
        self.cursor.execute("""INSERT INTO certificados ('cod','nome_aluno','nome_treinador') VALUES(?,?,?)""",(self.codigo,self.aluno,self.instrutor))
        self.conn.commit()
        self.desconectaDB()
        self.listarCertificados()
        self.limpa_telaSemPergunta()
    def listarCertificados(self):
        self.listaC.delete(*self.listaC.get_children())
        self.conectaDB()
        lista = self.cursor.execute("""SELECT * FROM certificados ORDER BY nome_aluno""")    
        for certificado in lista:
            self.listaC.insert("",END,values=certificado)
        self.desconectaDB()    
    #
    def onDoubleclick(self):
        self.limpa_tela()
        self.listaC.selection()
        

        for tupla in self.listaC.selection():
            col1,col2,col3 = tupla

class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.componentesTela()
        self.lista_frame2()
        self.montaTabela()
        root.mainloop()

    def tela(self):
        root.configure(background='#87CEEB')
        root.title("Certificados")
        root.geometry('1000x600')
        root.resizable(True, True)

    def componentesTela(self):
        # criando frame para a tela
        self.frame = Frame(root)
        self.frame.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.5)
      
        self.frame2 = Frame(root)
        self.frame2.place(relx=0.1, rely=0.53, relwidth=0.8, relheight=0.46)
        # criando botões
        self.btLipar = Button(self.frame, text='Limpar', fg='black', font=(
            'Arial', 9, 'bold'), command=self.limpa_tela,background='#87CEEB')
        self.btLipar.place(relx=0.3, rely=0.03, relwidth=0.1, relheight=0.09)
       
        self.btBuscar = Button(self.frame,text='Buscar', fg='black',background='#87CEEB', font=(
            'Arial', 9, 'bold'), command=self.listarCertificados) 
        self.btBuscar.place(relx=0.43, rely=0.03, relwidth=0.1, relheight=0.09)
       
        self.btAdicionar = Button(self.frame,text='Adicionar', fg='black',background='#87CEEB', font=(
            'Arial', 9, 'bold'), command=self.addCertificado)
        self.btAdicionar.place(relx=0.57, rely=0.03, relwidth=0.1, relheight=0.09)    
       
        self.btAltualizar = Button(self.frame,text='Atualizar', fg='black',background='#87CEEB', font=(
            'Arial', 9, 'bold'))
        self.btAltualizar.place(relx=0.70, rely=0.03, relwidth=0.1, relheight=0.09)   


        self.btApagar = Button(self.frame,text='Apagar', fg='black',background='#87CEEB', font=(
            'Arial', 9, 'bold'))
        self.btApagar.place(relx=0.83, rely=0.03, relwidth=0.1, relheight=0.09)

        # criando labels 
        self.lb_codigo = Label(self.frame, text='Código', font=('Arial', 9, 'bold'))
        self.lb_codigo.place(relx=0.10, rely=0.03, relwidth=0.1, relheight=0.09)

        self.inp_codigo = Entry(self.frame)
        self.inp_codigo.place(relx=0.10, rely=0.16, relwidth=0.15, relheight=0.09)

        self.lb_nomeAluno = Label(self.frame, text='Nome do Aluno', font=('Arial', 9, 'bold'))
        self.lb_nomeAluno.place(relx=0.09, rely=0.35, relwidth=0.18, relheight=0.09)

        self.lb_nomeCurso =   Label(self.frame, text='Nome do Aluno', font=('Arial', 9, 'bold'))     
        self.lb_nomeCurso.place(relx=0.09, rely=0.35, relwidth=0.18, relheight=0.09)  
        
        #criando inputs
        self.inp_nomeAluno = Entry(self.frame, font=('Arial' ,9))
        self.inp_nomeAluno.place(relx=0.10, rely=0.45, relwidth=0.4, relheight=0.09)

        self.lb_instrutor = Label(self.frame, text='Nome do Treinador', font=('Arial', 9, 'bold'))
        self.lb_instrutor.place(relx=0.09, rely=0.65, relwidth=0.2, relheight=0.09)
      
        self.inp_instrutor = Entry(self.frame, font=('Arial' ,9))
        self.inp_instrutor.place(relx=0.10, rely=0.75, relwidth=0.4, relheight=0.09)
    def lista_frame2(self):
        #criando lista  e definidno as colunas  
        self.listaC = ttk.Treeview(self.frame2,height=3,columns=('col1','col2','col3','col4'))
        self.listaC.heading('#0',text='')
        self.listaC.heading('#1',text='Codigo')
        self.listaC.heading('#2',text='Nome Aluno')
        self.listaC.heading('#3',text='Treinador')
        #definindo o tamanho das colunas e a posição da lista
        self.listaC.column('#0', width=1)
        self.listaC.column('#1', width=50)
        self.listaC.column('#2', width=200)
        self.listaC.column('#3', width=200)
        self.listaC.place(relx=0.01, rely=0.1,relwidth=0.95,relheight=0.85)
        # criando scrollbar da listaC
        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaC.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1,relwidth=0.05,relheight=0.85)
Aplication()