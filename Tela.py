from mailbox import mboxMessage
from operator import iconcat
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tokenize import String
import sqlite3
from turtle import ondrag
from Funcs import Funcs
from reportlab.pdfgen import canvas
from reportlab.pdfbase import letters, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
root = Tk()

class Relatorios():
    

class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.componentesTela()
        self.lista_frame2()
        self.montaTabela()
        self.listarCertificados()
        root.mainloop()

    def tela(self):
        root.configure(background='#87CEEB')
        root.title("Certificados")
        root.geometry('1000x600')
        root.resizable(True, True)
        root.minsize(width=800, height=500)

    def componentesTela(self):
        # criando frame para a tela
        self.frame = Frame(root)
        self.frame.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.5)

        self.frame2 = Frame(root)
        self.frame2.place(relx=0.1, rely=0.53, relwidth=0.8, relheight=0.46)
        # criando botões
        self.btLipar = Button(self.frame, text='Limpar', fg='black', font=(
            'Arial', 9, 'bold'), command=self.limpa_tela, background='#87CEEB')
        self.btLipar.place(relx=0.3, rely=0.03, relwidth=0.1, relheight=0.09)

        self.btBuscar = Button(self.frame, text='Buscar', fg='black', background='#87CEEB', font=(
            'Arial', 9, 'bold'), command=self.listarCertificados)
        self.btBuscar.place(relx=0.43, rely=0.03, relwidth=0.1, relheight=0.09)

        self.btAdicionar = Button(self.frame, text='Adicionar', fg='black', background='#87CEEB', font=(
            'Arial', 9, 'bold'), command=self.addCertificado)
        self.btAdicionar.place(relx=0.57, rely=0.03,
                               relwidth=0.1, relheight=0.09)

        self.btAltualizar = Button(self.frame, text='Atualizar', fg='black', background='#87CEEB', font=(
            'Arial', 9, 'bold'), command=self.alterarDados)
        self.btAltualizar.place(relx=0.70, rely=0.03,
                                relwidth=0.1, relheight=0.09)

        self.btApagar = Button(self.frame, text='Apagar', fg='black', background='#87CEEB', font=(
            'Arial', 9, 'bold'), command=self.deletaCertificado)
        self.btApagar.place(relx=0.83, rely=0.03, relwidth=0.1, relheight=0.09)

        self.btGerarCertificado = Button(self.frame, text='Gerar Certificado', fg='black', background='#87CEEB',
                                         font=('Arial', 9, 'bold'))
        self.btGerarCertificado.place(relx=0.73, rely=0.4, relwidth=0.2, relheight=0.09)

        # criando labels
        self.lb_codigo = Label(self.frame, text='Código',
                               font=('Arial', 9, 'bold'))
        self.lb_codigo.place(relx=0.10, rely=0.03,
                             relwidth=0.1, relheight=0.09)

        self.inp_codigo = Entry(self.frame)
        self.inp_codigo.place(relx=0.10, rely=0.16,
                              relwidth=0.15, relheight=0.09)

        self.lb_nomeAluno = Label(
            self.frame, text='Nome do Aluno', font=('Arial', 9, 'bold'))
        self.lb_nomeAluno.place(relx=0.09, rely=0.35,
                                relwidth=0.18, relheight=0.09)

        self.lb_nomeCurso = Label(
            self.frame, text='Nome do Aluno', font=('Arial', 9, 'bold'))
        self.lb_nomeCurso.place(relx=0.09, rely=0.35,
                                relwidth=0.18, relheight=0.09)

        # criando inputs
        self.inp_nomeAluno = Entry(self.frame, font=('Arial', 9))
        self.inp_nomeAluno.place(relx=0.10, rely=0.45,
                                 relwidth=0.4, relheight=0.09)

        self.lb_instrutor = Label(
            self.frame, text='Nome do Treinador', font=('Arial', 9, 'bold'))
        self.lb_instrutor.place(relx=0.09, rely=0.65,
                                relwidth=0.2, relheight=0.09)

        self.inp_instrutor = Entry(self.frame, font=('Arial', 9))
        self.inp_instrutor.place(relx=0.10, rely=0.75,
                                 relwidth=0.4, relheight=0.09)

    def lista_frame2(self):
        # criando lista  e definidno as colunas
        self.listaC = ttk.Treeview(
            self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listaC.heading('#0', text='')
        self.listaC.heading('#1', text='Codigo')
        self.listaC.heading('#2', text='Nome Aluno')
        self.listaC.heading('#3', text='Treinador')
        # definindo o tamanho das colunas e a posição da lista
        self.listaC.column('#0', width=1)
        self.listaC.column('#1', width=50)
        self.listaC.column('#2', width=200)
        self.listaC.column('#3', width=200)
        self.listaC.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        # criando scrollbar da listaC
        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaC.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1,
                               relwidth=0.05, relheight=0.85)
        self.listaC.bind("<Double-1>", func=self.onDoubleclick)

    # def Menus(self):
    #     menubar = Menu(self.root)
    #     self.root.config(menu=menubar)
    #     mnFrente = Menu(menubar)
    #     mnVerso=
    #     def Quite(): self.root.destroy()
    #     menubar.add_cascade()
Aplication()
