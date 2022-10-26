
from mailbox import mboxMessage
from operator import iconcat
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tokenize import String
import sqlite3
class Funcs():
    def variaveis(self):
        self.codigo = self.inp_codigo.get()
        self.aluno = self.inp_nomeAluno.get()
        self.instrutor = self.inp_instrutor.get()
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
            cod CHAR(4) NOT NULL PRIMARY KEY,
            nome_aluno CHAR(40) NOT NULL,
            nome_treinador CHAR(40) NOT NULL
        )""")
        self.conn.commit()
        self.desconectaDB()
    def addCertificado(self):
        self.variaveis()

        if len(self.codigo)==4:
            self.conectaDB()
            self.cursor.execute("""INSERT INTO certificados ('cod','nome_aluno','nome_treinador') VALUES(?,?,?)""",(self.codigo,self.aluno,self.instrutor))
            self.conn.commit()
            self.desconectaDB()
            self.listarCertificados()
            self.limpa_telaSemPergunta()
        else:
            mb.showinfo('Aviso','Codigo inválido')
            self.inp_codigo.focus()
                
    def listarCertificados(self):
        self.listaC.delete(*self.listaC.get_children())
        self.conectaDB()
        lista = self.cursor.execute("""SELECT * FROM certificados ORDER BY nome_aluno""")    
        for certificado in lista:
            self.listaC.insert("",END,values=certificado)
        self.desconectaDB()    
    #
    def onDoubleclick(self,event):
        self.limpa_telaSemPergunta()
        self.listaC.selection()
        for tupla in self.listaC.selection():
            col1,col2,col3 = self.listaC.item(tupla,'values')
            self.inp_codigo.insert(END,col1)
            self.inp_nomeAluno.insert(END,col2)
            self.inp_instrutor.insert(END,col3)
    def deletaCertificado(self):
        res = mb.askquestion('Limpar Dados','Deseja realmente excluir os dados desse certificado?')
        if(res=='yes'):
            self.variaveis()
            self.conectaDB()
            self.cursor.execute("""DELETE FROM certificados WHERE cod = ? """,[(self.codigo)])
            self.conn.commit()
            self.desconectaDB()
            self.limpa_telaSemPergunta()
            self.listarCertificados()
    def alterarDados(self):
        self.variaveis()
        self.conectaDB()
        print(self.codigo)
        print(self.aluno)
        print(self.instrutor)
        self.cursor.execute("""UPDATE certificados SET nome_aluno = ?, nome_treinador = ? WHERE cod = ? """,(self.aluno,self.instrutor,self.codigo))
        self.conn.commit()
        self.desconectaDB()
        self.listarCertificados()
        self.limpa_telaSemPergunta()
