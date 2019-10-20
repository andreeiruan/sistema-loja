from tkinter import *
import funcionarios
import clientes
import produtos


def prod():
    """Essas funções são para abrir as opções de cada tabela"""
    return produtos.Produtos()


def func():
    return funcionarios.Funcionarios()


def cli():
    return clientes.Clientes()


class Menu:
    def __init__(self):
        self.fonte = ('Verdana', '10')

        self.janela = Tk()
        self.janela.title('Sistema Loja')
        self.janela.geometry('400x350+450+200')
        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Sistema da loja')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 15
        self.c2.pack()
        self.funcionarios = Button(self.c2, text='Funcionários', font=self.fonte, width=20)
        self.funcionarios['command'] = func
        self.funcionarios.pack()

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 15
        self.c3.pack()
        self.produtos = Button(self.c3, text='Produtos', font=self.fonte, width=20)
        self.produtos['command'] = prod
        self.produtos.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 15
        self.c4.pack()
        self.clientes = Button(self.c4, text='Clientes', font=self.fonte, width=20)
        self.clientes['command'] = cli
        self.clientes.pack()

        self.janela.mainloop()
