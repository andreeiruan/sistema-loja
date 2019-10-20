from tkinter import *
import funcoes
import query
from pymysql import err


def buscar():
    return BuscarProduto()


def adicionar():
    return InserirProduto()


def alterar():
    return BuscarProdutoAlterar()


def excluir():
    return BuscaExcluirProduto()


janela_confirmar = None


class Produtos:

    def __init__(self):
        self.fonte = ('Verdana', '10')

        self.janela = Tk()
        self.janela.title('Produtos')
        self.janela.geometry('400x350+450+200')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.busc = Button(self.c2, text='Buscar', font=self.fonte, width=20)
        self.busc['command'] = buscar
        self.busc.pack()

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.add = Button(self.c3, text='Adicionar', font=self.fonte, width=20)
        self.add['command'] = adicionar
        self.add.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.alt = Button(self.c4, text='Alterar', font=self.fonte, width=20)
        self.alt['command'] = alterar
        self.alt.pack()

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 5
        self.c5.pack()
        self.exc = Button(self.c5, text='Excluir', font=self.fonte, width=20)
        self.exc['command'] = excluir
        self.exc.pack()


class BuscarProduto:

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Produtos')
        self.janela.geometry('400x200+450+250')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Produtos')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbcod = Label(self.c2, text='Codigo', font=self.fonte, width=5)
        self.lbcod.pack(side=LEFT)
        self.txtcod = Entry(self.c2, width=30, font=self.fonte)
        self.txtcod.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=10)
        self.busc['command'] = self.busca
        self.busc.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.msg = Label()

        self.janela.mainloop()

    def busca(self):
        from inicio import servidor
        self.msg.destroy()
        cod = str(self.txtcod.get()).strip()
        f = funcoes.pegar_dados_produto(cod, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='Codigo do produto não encontrado nos registros', width=50, font=self.fonte,
                             fg='red')
            return self.msg.pack()
        else:
            return ResultadoBuscaProduto(f['codigo'], f['nome'], f['marca'], f['preco'], f['descricao'], f['estoque'])


class ResultadoBuscaProduto:

    def __init__(self, codigo, nome, marca, preco, desc, estoque):
        self.janela = Tk()
        self.janela.title(f"Produto {nome}")
        self.janela.geometry('500x500+400+100')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'Produto {nome}')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbid = Label(self.c2, text='Codigo', font=self.fonte, width=30)
        self.lbid.pack(side=LEFT)
        self.txtid = Label(self.c2, text=codigo,
                           font=self.fonte, width=30, bg='white')
        self.txtid.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.lbnome = Label(self.c3, text='Nome', font=self.fonte, width=30)
        self.lbnome.pack(side=LEFT)
        self.txtnome = Label(self.c3, text=nome,
                             font=self.fonte, width=30, bg='white')
        self.txtnome.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.lbmar = Label(self.c4, text='Marca', font=self.fonte, width=30)
        self.lbmar.pack(side=LEFT)
        self.txtmar = Label(self.c4, text=marca,
                            font=self.fonte, width=30, bg='white')
        self.txtmar.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 5
        self.c5.pack()
        self.lbpr = Label(self.c5, text='Preço', font=self.fonte, width=30)
        self.lbpr.pack(side=LEFT)
        self.txtpr = Label(self.c5, text=preco,
                           font=self.fonte, width=30, bg='white')
        self.txtpr.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 5
        self.c6.pack()
        self.lbdes = Label(self.c6, text='Descrição',
                           font=self.fonte, width=30)
        self.lbdes.pack(side=LEFT)
        self.txtdes = Label(self.c6, text=desc,
                            font=self.fonte, width=30, bg='white')
        self.txtdes.pack(side=LEFT)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 5
        self.c7.pack()
        self.lbes = Label(self.c7, text='Estoque', font=self.fonte, width=30)
        self.lbes.pack(side=LEFT)
        self.txtes = Label(self.c7, text=estoque,
                           font=self.fonte, width=30, bg='white')
        self.txtes.pack(side=LEFT)

        self.janela.mainloop()


class InserirProduto:

    def __init__(self):
        self.janela = Tk()
        self.janela.title(f"Cadastro de Produto!")
        self.janela.geometry('500x500+400+100')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'Cadastrar Produto')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbnome = Label(self.c2, text='Nome', font=self.fonte, width=20)
        self.lbnome.pack(side=LEFT)
        self.nome = Entry(self.c2, font=self.fonte, width=20)
        self.nome.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.lbmar = Label(self.c3, text='Marca', font=self.fonte, width=20)
        self.lbmar.pack(side=LEFT)
        self.mar = Entry(self.c3, font=self.fonte, width=20)
        self.mar.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.lbpr = Label(self.c4, text='Preço R$', font=self.fonte, width=20)
        self.lbpr.pack(side=LEFT)
        self.pr = Entry(self.c4, font=self.fonte, width=20)
        self.pr.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 5
        self.c5.pack()
        self.lbdes = Label(self.c5, text='Descrição',
                           font=self.fonte, width=20)
        self.lbdes.pack(side=LEFT)
        self.desc = Entry(self.c5, font=self.fonte, width=20)
        self.desc.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 5
        self.c6.pack()
        self.lbes = Label(self.c6, text='Estoque', font=self.fonte, width=20)
        self.lbes.pack(side=LEFT)
        self.est = Entry(self.c6, font=self.fonte, width=20)
        self.est.pack(side=LEFT)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 15
        self.c7.pack()
        self.inserir = Button(self.c7, text='Cadastrar', width=20, font=self.fonte)
        self.inserir['command'] = self.insert
        self.inserir.pack()

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 10
        self.c8.pack()
        self.msg = Label()

        self.janela.mainloop()

    def insert(self):
        from inicio import servidor
        self.msg.destroy()

        nome = str(self.nome.get()).strip().title()
        if len(nome) == 0:
            self.msg = Label(self.c8, text='Campo nome esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()

        marca = str(self.mar.get()).strip().title()
        if len(marca) == 0:
            self.msg = Label(self.c8, text='Campo marca esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()

        preco = str(self.pr.get()).strip()
        if len(preco) == 0:
            self.msg = Label(self.c8, text='Campo preço esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()
        else:
            preco_temp = preco.split(',')
            if len(preco_temp) == 1:
                pass
            else:
                if len(preco_temp[1]) > 2:
                    self.msg = Label(self.c8, text='Use apenas duas casas decimais pra indicar os centavos',
                                     font=self.fonte, width=60, fg='red')
                    return self.msg.pack()
            for num in preco_temp:
                for n in num:
                    if not n.isnumeric():
                        self.msg = Label(self.c8, text='Use valor numerico para definir o valor',
                                         font=self.fonte, width=40, fg='red')
                        return self.msg.pack()

        descricao = str(self.desc.get())
        if len(descricao) == 0:
            self.msg = Label(self.c8, text='Campo descrição esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()

        estoque = str(self.est.get())
        if len(estoque) == 0:
            self.msg = Label(self.c8, text='Campo estoque esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()
        else:
            if not estoque.isnumeric():
                self.msg = Label(self.c8, text='Campo estoque precisa ser um valor inteiro', font=self.fonte,
                                 width=40, fg='red')
                return self.msg.pack()
        try:
            query.insert_produto(nome, marca, preco.replace(',', '.'), descricao, estoque,
                                 servidor.host, servidor.usr, servidor.passwd)
        except err.InternalError:
            self.msg = Label(self.c8, text='Ocorreu algum erro, verifique se os dados estao corretos', font=self.fonte,
                             width=60, fg='red')
            return self.msg.pack()
        else:
            self.msg = Label(self.c8, text='Dados Inseridos com sucesso', width=40, font=self.fonte, fg='green')
            self.nome.delete(0, END)
            self.mar.delete(0, END)
            self.pr.delete(0, END)
            self.desc.delete(0, END)
            self.est.delete(0, END)
            return self.msg.pack()


class BuscarProdutoAlterar:

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Produtos')
        self.janela.geometry('400x200+450+250')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Produtos')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbcod = Label(self.c2, text='Codigo', font=self.fonte, width=5)
        self.lbcod.pack(side=LEFT)
        self.txtcod = Entry(self.c2, width=30, font=self.fonte)
        self.txtcod.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=10)
        self.busc['command'] = self.busca
        self.busc.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.msg = Label()

        self.janela.mainloop()

    def busca(self):
        from inicio import servidor
        self.msg.destroy()
        codigo = str(self.txtcod.get()).strip()
        f = funcoes.pegar_dados_produto(codigo, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='Codigo de produto não encontrado', width=40, fg='red', font=self.fonte)
            return self.msg.pack()
        return AlterarProduto(f['codigo'], f['nome'], f['marca'], f['preco'], f['descricao'], f['estoque'])


class AlterarProduto:

    def __init__(self, codigo, nome, marca, preco, desc, estoque):
        preco = preco[2:]
        self.janela = Tk()
        self.janela.title(f"Cadastro de Produto!")
        self.janela.geometry('500x500+400+100')
        self.codigo = codigo

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'Cadastrar Produto')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbnome = Label(self.c2, text='Nome', font=self.fonte, width=20)
        self.lbnome.pack(side=LEFT)
        self.nome = Entry(self.c2, font=self.fonte, width=20)
        self.nome.pack(side=LEFT)
        self.nome.insert(INSERT, nome)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.lbmar = Label(self.c3, text='Marca', font=self.fonte, width=20)
        self.lbmar.pack(side=LEFT)
        self.mar = Entry(self.c3, font=self.fonte, width=20)
        self.mar.pack(side=LEFT)
        self.mar.insert(INSERT, marca)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.lbpr = Label(self.c4, text='Preço R$', font=self.fonte, width=20)
        self.lbpr.pack(side=LEFT)
        self.pr = Entry(self.c4, font=self.fonte, width=20)
        self.pr.pack(side=LEFT)
        self.pr.insert(INSERT, preco)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 5
        self.c5.pack()
        self.lbdes = Label(self.c5, text='Descrição', font=self.fonte, width=20)
        self.lbdes.pack(side=LEFT)
        self.desc = Entry(self.c5, font=self.fonte, width=20)
        self.desc.pack(side=LEFT)
        self.desc.insert(INSERT, desc)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 5
        self.c6.pack()
        self.lbes = Label(self.c6, text='Estoque', font=self.fonte, width=20)
        self.lbes.pack(side=LEFT)
        self.est = Entry(self.c6, font=self.fonte, width=20)
        self.est.pack(side=LEFT)
        self.est.insert(INSERT, estoque)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 15
        self.c7.pack()
        self.inserir = Button(self.c7, text='Alterar', width=20, font=self.fonte)
        self.inserir['command'] = self.update
        self.inserir.pack()

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 10
        self.c8.pack()
        self.msg = Label()

        self.janela.mainloop()

    def update(self):
        from inicio import servidor
        self.msg.destroy()
        codigo = self.codigo

        nome = str(self.nome.get()).strip().title()
        if len(nome) == 0:
            self.msg = Label(self.c8, text='Campo nome esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()

        marca = str(self.mar.get()).strip().title()
        if len(marca) == 0:
            self.msg = Label(self.c8, text='Campo marca esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()

        preco = str(self.pr.get()).strip()
        if len(preco) == 0:
            self.msg = Label(self.c8, text='Campo preço esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()
        else:
            preco_temp = preco.split(',')
            if len(preco_temp) == 1:
                pass
            else:
                if len(preco_temp[1]) > 2:
                    self.msg = Label(self.c8, text='Use apenas duas casas decimais pra indicar os centavos',
                                     font=self.fonte, width=60, fg='red')
                    return self.msg.pack()
            for num in preco_temp:
                for n in num:
                    if not n.isnumeric():
                        self.msg = Label(self.c8, text='Use valor numerico para definir o valor',
                                         font=self.fonte, width=40, fg='red')
                        return self.msg.pack()

        descricao = str(self.desc.get())
        if len(descricao) == 0:
            self.msg = Label(self.c8, text='Campo descrição esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()

        estoque = str(self.est.get())
        if len(estoque) == 0:
            self.msg = Label(self.c8, text='Campo estoque esta vazio', font=self.fonte, width=40, fg='red')
            return self.msg.pack()
        else:
            if not estoque.isnumeric():
                self.msg = Label(self.c8, text='Campo estoque precisa ser um valor inteiro', font=self.fonte,
                                 width=40, fg='red')
                return self.msg.pack()
        try:
            query.update_produto(codigo, nome, marca, preco.replace(',', '.'), descricao, estoque,
                                 servidor.host, servidor.usr, servidor.passwd)
        except err.InternalError:
            self.msg = Label(self.c8, text='Ocorreu algum erro', font=self.fonte,
                             width=40, fg='red')
            return self.msg.pack()
        else:
            self.janela.destroy()
            janela_sucesso = Tk()
            janela_sucesso.title('Sucesso')
            janela_sucesso.geometry('300x80+500+350')
            lb = Label(janela_sucesso, width=50, font=('calibru', '10', 'bold'),
                       text='Dados Alterados com sucesso', fg='green')
            lb.pack()
            button = Button(janela_sucesso, width=20, font=('calibru', '8', 'bold'), text='OK')
            button['command'] = janela_sucesso.destroy
            button.pack()
            janela_sucesso.mainloop()


class BuscaExcluirProduto:

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Produtos')
        self.janela.geometry('400x200+450+250')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Produtos')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbcod = Label(self.c2, text='Codigo', font=self.fonte, width=5)
        self.lbcod.pack(side=LEFT)
        self.txtcod = Entry(self.c2, width=30, font=self.fonte)
        self.txtcod.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=10)
        self.busc['command'] = self.busca
        self.busc.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.msg = Label()

        self.janela.mainloop()

    def busca(self):
        from inicio import servidor
        self.msg.destroy()
        codigo = str(self.txtcod.get()).strip()
        f = funcoes.pegar_dados_produto(codigo, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='Codigo de produto não encontrado', width=40, fg='red', font=self.fonte)
            return self.msg.pack()
        return ExcluirProduto(f['codigo'], f['nome'], f['marca'], f['preco'], f['descricao'], f['estoque'])


class ExcluirProduto:

    def __init__(self, cod, nome, marca, preco, desc, estoque):
        preco = preco[2:]
        self.janela = Tk()
        self.janela.title(f"Cadastro de Produto!")
        self.janela.geometry('500x500+400+100')
        self.codigo = cod

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'Cadastrar Produto')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbnome = Label(self.c2, text='Nome', font=self.fonte, width=20)
        self.lbnome.pack(side=LEFT)
        self.nome = Label(self.c2, text=nome, font=self.fonte, width=20)
        self.nome.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.lbmar = Label(self.c3, text='Marca', font=self.fonte, width=20)
        self.lbmar.pack(side=LEFT)
        self.mar = Label(self.c3, text=marca, font=self.fonte, width=20)
        self.mar.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.lbpr = Label(self.c4, text='Preço R$', font=self.fonte, width=20)
        self.lbpr.pack(side=LEFT)
        self.pr = Label(self.c4, text=preco, font=self.fonte, width=20)
        self.pr.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 5
        self.c5.pack()
        self.lbdes = Label(self.c5, text='Descrição', font=self.fonte, width=20)
        self.lbdes.pack(side=LEFT)
        self.desc = Label(self.c5, text=desc, font=self.fonte, width=20)
        self.desc.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 5
        self.c6.pack()
        self.lbes = Label(self.c6, text='Estoque', font=self.fonte, width=20)
        self.lbes.pack(side=LEFT)
        self.est = Label(self.c6, text=estoque, font=self.fonte, width=20)
        self.est.pack(side=LEFT)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 15
        self.c7.pack()
        self.exc = Button(self.c7, text='Alterar', width=20, font=self.fonte)
        self.exc['command'] = self.confirma
        self.exc.pack()

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 10
        self.c8.pack()
        self.msg = Label()

        self.janela.mainloop()

    def confirma(self):
        global janela_confirmar
        janela_confirmar = Tk()
        janela_confirmar.title('Confirmação')
        janela_confirmar.geometry('250x100+520+300')
        lb = Label(janela_confirmar, text='Deseja mesmo excluir os dados?', width=30, font=self.fonte)
        lb.place(x=12, y=18)
        sim = Button(janela_confirmar, text='Sim', width=5, font=self.fonte, command=self.remove)
        sim.place(x=78, y=50)
        nao = Button(janela_confirmar, text='Não', width=5, font=self.fonte)
        nao.place(x=128, y=50)
        janela_confirmar.mainloop()

    def remove(self):
        janela_confirmar.destroy()
        from inicio import servidor
        query.delete_produto(self.codigo, servidor.host, servidor.usr, servidor.passwd)
        self.janela.destroy()
        janela_sucesso = Tk()
        lb = Label(janela_sucesso, text='Dados excluidos com sucesso',
                   width=60, font=('calibru', '9', 'bold'), fg='green')
        lb.pack()
        btn = Button(janela_sucesso, text='OK', font=self.fonte, command=janela_sucesso.destroy)
        btn.pack()
        janela_sucesso.geometry('300x80+500+350')
        janela_sucesso.mainloop()
