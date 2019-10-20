from tkinter import *
import funcoes
from pymysql import err
import query


def buscar():
    return BuscarCliente()


def adicionar():
    return InserirCliente()


def alterar():
    return BuscaAlteraCliente()


def excluir():
    pass


janela_confirmar = None


class Clientes:

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Clientes')
        self.janela.geometry('400x350+450+200')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Clientes')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.busc = Button(self.c2, text='Buscar', font=self.fonte, width=20)
        self.busc['command'] = buscar
        self.busc.pack()

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.add = Button(self.c3, text='Adicionar', font=self.fonte, width=20)
        self.add['command'] = adicionar
        self.add.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.alt = Button(self.c4, text='Alterar', font=self.fonte, width=20)
        self.alt['command'] = alterar
        self.alt.pack()

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.exc = Button(self.c5, text='Excluir', font=self.fonte, width=20)
        self.exc['command'] = excluir
        self.exc.pack()

        self.janela.mainloop()


class BuscarCliente:

    def __init__(self):
        self.fonte = ('Verdana', '10')
        self.janela = Tk()
        self.janela.title('Clientes')
        self.janela.geometry('400x200+450+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Clientes')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbcpf = Label(self.c2, text='CPF', font=self.fonte, width=5)
        self.lbcpf.pack(side=LEFT)
        self.txtcpf = Entry(self.c2, width=30, font=self.fonte)
        self.txtcpf.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=10)
        self.busc['command'] = self.busca
        self.busc.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.msg = Label()

        self.janela.mainloop()

    def busca(self):
        from inicio import servidor
        cpf = self.txtcpf.get()
        f = funcoes.pegar_dados_clientes(cpf, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='CPF não encontrado nos registros',
                             width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            return ResultadoBuscaCliente(f['id'], f['nome'], f['sobrenome'], f['cpf'],  f['email'],
                                         f['telefone'], f['nasc'])


class ResultadoBuscaCliente:

    def __init__(self, codigo, nome, sobrenome, cpf, email, telefone, nasc):
        self.janela = Tk()
        self.janela.title(f"Dados do Cliente {nome}")
        self.janela.geometry('500x500+400+100')
        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'Cliente {nome}')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbid = Label(self.c2, text='ID', font=self.fonte, width=30)
        self.lbid.pack(side=LEFT)
        self.txtid = Label(self.c2, text=codigo,
                           font=self.fonte, width=30, bg='white')
        self.txtid.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.lbnome = Label(self.c3, text='Nome', font=self.fonte, width=30)
        self.lbnome.pack(side=LEFT)
        self.txtnome = Label(self.c3, text=nome,
                             font=self.fonte, width=30, bg='white')
        self.txtnome.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.lbsobrenome = Label(
            self.c4, text='Sobrenome', font=self.fonte, width=30)
        self.lbsobrenome.pack(side=LEFT)
        self.txtsobrenome = Label(
            self.c4, text=sobrenome, font=self.fonte, width=30, bg='white')
        self.txtsobrenome.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.lbcpf = Label(self.c5, text='CPF', font=self.fonte, width=30)
        self.lbcpf.pack(side=LEFT)
        self.txtcpf = Label(self.c5, text=cpf,
                            font=self.fonte, width=30, bg='white')
        self.txtcpf.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 7
        self.c6.pack()
        self.lbtel = Label(self.c6, text='Telefone', font=self.fonte, width=30)
        self.lbtel.pack(side=LEFT)
        self.txttel = Label(self.c6, text=telefone,
                            font=self.fonte, width=30, bg='white')
        self.txttel.pack(side=LEFT)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 7
        self.c7.pack()
        self.lbemail = Label(self.c7, text='Email', font=self.fonte, width=30)
        self.lbemail.pack(side=LEFT)
        self.txtemail = Label(self.c7, text=email,
                              font=self.fonte, width=30, bg='white')
        self.txtemail.pack(side=LEFT)

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 7
        self.c8.pack()
        self.lbdn = Label(self.c8, text='Data de Nascimento',
                          font=self.fonte, width=30)
        self.lbdn.pack(side=LEFT)
        self.txtdn = Label(self.c8, text=nasc,
                           font=self.fonte, width=30, bg='white')
        self.txtdn.pack(side=LEFT)

        self.janela.mainloop()


class InserirCliente:

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Cadastro de Clientes')
        self.janela.geometry('500x500+400+100')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Cadastro de Clientes',
                            width=30, font=('calibru', '16', 'bold'))
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbnome = Label(self.c2, text='Nome', width=20, font=self.fonte)
        self.lbnome.pack(side=LEFT)
        self.nome = Entry(self.c2, font=self.fonte, width=20)
        self.nome.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.lbsobre = Label(self.c3, text='Sobrenome',
                             width=20, font=self.fonte)
        self.lbsobre.pack(side=LEFT)
        self.sobre = Entry(self.c3, font=self.fonte, width=20)
        self.sobre.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.lbcpf = Label(self.c4, text='CPF', width=20, font=self.fonte)
        self.lbcpf.pack(side=LEFT)
        self.cpf = Entry(self.c4, width=20, font=self.fonte)
        self.cpf.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.lbemail = Label(self.c5, text='Email', width=20, font=self.fonte)
        self.lbemail.pack(side=LEFT)
        self.email = Entry(self.c5, width=20, font=self.fonte)
        self.email.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 7
        self.c6.pack()
        self.lbtel = Label(self.c6, text='Telefone', width=20, font=self.fonte)
        self.lbtel.pack(side=LEFT)
        self.tel = Entry(self.c6, width=20, font=self.fonte)
        self.tel.pack(side=LEFT)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 7
        self.c7.pack()
        self.lbnasc = Label(self.c7, text='Data de Nascimento',
                            width=20, font=self.fonte)
        self.lbnasc.pack(side=LEFT)
        self.nasc = Entry(self.c7, width=20, font=self.fonte)
        self.nasc.pack(side=LEFT)

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 7
        self.c8.pack()
        self.inserir = Button(self.c8, text='Inserir',
                              width=20, font=self.fonte, command=self.insert)
        self.inserir.pack()

        self.c9 = Frame(self.janela)
        self.c9['pady'] = 15
        self.c9.pack()
        self.msg = Label()
        self.msg2 = Label()

        self.janela.mainloop()

    def insert(self):
        from inicio import servidor
        self.msg.destroy()
        self.msg2.destroy()

        nome = str(self.nome.get()).strip().title()
        if len(nome) == 0:
            self.msg = Label(self.c9, text='Campo nome esta vazio',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()

        sobrenome = str(self.sobre.get()).strip().title()
        if len(sobrenome) == 0:
            self.msg = Label(self.c9, text='Campo sobrenome esta vazio',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()

        cpf = str(self.cpf.get()).strip().replace('-', '')
        if len(cpf) != 11:
            self.msg = Label(self.c9, text='Campo CPF esta incorreto',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            for c in cpf:
                if not c.isnumeric():
                    self.msg = Label(
                        self.c9, text='Campo CPF esta incorreto', width=45, font=self.fonte, fg='red')
                    return self.msg.pack()

        email = str(self.email.get()).strip()
        if len(email) == 0:
            email = 'Null'

        tel = str(self.tel.get()).strip()
        if len(tel) != 11:
            self.msg = Label(self.c9, text='Campo telefone esta incorreto',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            for n in tel:
                if not n.isnumeric():
                    self.msg = Label(
                        self.c9, text='Campo telefone esta incorreto', width=45, font=self.fonte, fg='red')
                    return self.msg.pack()
            if tel[0] not in '5' and tel[1] not in '1':
                self.msg = Label(
                    self.c9, text='Falta o ddd no telefone', width=45, font=self.fonte, fg='red')
                return self.msg.pack()

        nasc = str(self.nasc.get()).strip()
        try:
            nasc = funcoes.inverter_datas(nasc)
        except IndexError:
            self.msg = Label(self.c9, text='Formato das datas estão invalidos',
                             width=30, font=self.fonte, fg='red')
            self.msg.pack()
            self.msg2 = Label(
                self.c9, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
            self.msg2.pack()
        else:
            try:
                query.insert_cliente(nome, sobrenome, cpf, tel, nasc, email,
                                     servidor.host, servidor.usr, servidor.passwd)
            except err.InternalError:
                self.msg = Label(self.c9, text='Formato das datas estão invalidos', width=30,
                                 font=self.fonte, fg='red')
                self.msg.pack()
                self.msg2 = Label(
                    self.c9, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
                self.msg2.pack()

            except err.IntegrityError:
                self.msg = Label(self.c9, text='Este cpf já esta cadastrado', width=30,
                                 font=self.fonte, fg='red')
                self.msg.pack()

            else:
                self.msg2 = Label(
                    self.c9, text='Dados inseridos com sucesso', width=30, font=self.fonte, fg='green')
                self.msg2.pack()


class BuscaAlteraCliente:

    def __init__(self):
        self.fonte = ('Verdana', '10')
        self.janela = Tk()
        self.janela.title('Clientes')
        self.janela.geometry('400x200+450+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Clientes')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbcpf = Label(self.c2, text='CPF', font=self.fonte, width=5)
        self.lbcpf.pack(side=LEFT)
        self.txtcpf = Entry(self.c2, width=30, font=self.fonte)
        self.txtcpf.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=10)
        self.busc['command'] = self.busca
        self.busc.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.msg = Label()

        self.janela.mainloop()

    def busca(self):
        from inicio import servidor
        cpf = self.txtcpf.get()
        f = funcoes.pegar_dados_clientes(cpf, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='CPF não encontrado nos registros',
                             width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            return AlterarCliente(f['id'], f['nome'], f['sobrenome'], f['cpf'], f['email'], f['telefone'], f['nasc'])


class AlterarCliente:

    def __init__(self, codigo, nome, sobrenome, cpf, email, telefone, nasc):
        self.janela = Tk()
        self.janela.title(f"Dados do Cliente {nome}")
        self.janela.geometry('500x500+400+100')

        self.codigo = codigo
        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 15
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'{nome} {sobrenome}')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbnome = Label(self.c2, text='Nome', font=self.fonte, width=30)
        self.lbnome.pack(side=LEFT)
        self.txtnome = Entry(self.c2, font=self.fonte, width=30)
        self.txtnome.pack(side=LEFT)
        self.txtnome.insert(INSERT, nome)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.lbsobrenome = Label(self.c3, text='Sobrenome', font=self.fonte, width=30)
        self.lbsobrenome.pack(side=LEFT)
        self.txtsobrenome = Entry(self.c3, font=self.fonte, width=30)
        self.txtsobrenome.pack(side=LEFT)
        self.txtsobrenome.insert(INSERT, sobrenome)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.lbcpf = Label(self.c4, text='CPF', font=self.fonte, width=30)
        self.lbcpf.pack(side=LEFT)
        self.txtcpf = Entry(self.c4, font=self.fonte, width=30)
        self.txtcpf.pack(side=LEFT)
        self.txtcpf.insert(INSERT, cpf)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.lbtel = Label(self.c5, text='Telefone', font=self.fonte, width=30)
        self.lbtel.pack(side=LEFT)
        self.txttel = Entry(self.c5, font=self.fonte, width=30)
        self.txttel.pack(side=LEFT)
        self.txttel.insert(INSERT, telefone)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 7
        self.c7.pack()
        self.lbemail = Label(self.c7, text='Email', font=self.fonte, width=30)
        self.lbemail.pack(side=LEFT)
        self.txtemail = Entry(self.c7, font=self.fonte, width=30)
        self.txtemail.pack(side=LEFT)
        self.txtemail.insert(INSERT, email)

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 7
        self.c8.pack()
        self.lbdn = Label(self.c8, text='Data de Nascimento',
                          font=self.fonte, width=30)
        self.lbdn.pack(side=LEFT)
        self.txtdn = Entry(self.c8, font=self.fonte, width=30)
        self.txtdn.pack(side=LEFT)
        self.txtdn.insert(INSERT, nasc)

        self.c9 = Frame(self.janela)
        self.c9['pady'] = 20
        self.c9.pack()
        self.alterar = Button(self.c9, text='Alterar',
                              font=self.fonte, width=20)
        self.alterar['command'] = self.update
        self.alterar.pack()

        self.c9 = Frame(self.janela)
        self.c9['pady'] = 7
        self.c9.pack()
        self.msg = Label()

        self.c10 = Frame(self.janela)
        self.c10['pady'] = 7
        self.c10.pack()
        self.msg2 = Label()

        self.janela.mainloop()

    def update(self):
        from inicio import servidor
        self.msg.destroy()
        self.msg2.destroy()
        codigo = self.codigo

        nome = str(self.txtnome.get()).strip().title()
        if len(nome) == 0:
            self.msg = Label(self.c9, text='Campo nome esta vazio',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()

        sobrenome = str(self.txtsobrenome.get()).strip().title()
        if len(sobrenome) == 0:
            self.msg = Label(self.c9, text='Campo sobrenome esta vazio',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()

        cpf = str(self.txtcpf.get()).strip().replace('-', '')
        if len(cpf) != 11:
            self.msg = Label(self.c9, text='Campo CPF esta incorreto',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            for c in cpf:
                if not c.isnumeric():
                    self.msg = Label(
                        self.c9, text='Campo CPF esta incorreto', width=45, font=self.fonte, fg='red')
                    return self.msg.pack()

        email = str(self.txtemail.get()).strip()
        if len(email) == 0:
            email = 'Null'

        tel = str(self.txttel.get()).strip()
        if len(tel) != 11:
            self.msg = Label(self.c9, text='Campo telefone esta incorreto',
                             width=45, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            for n in tel:
                if not n.isnumeric():
                    self.msg = Label(
                        self.c9, text='Campo telefone esta incorreto', width=45, font=self.fonte, fg='red')
                    return self.msg.pack()
            if tel[0] not in '5' and tel[1] not in '1':
                self.msg = Label(
                    self.c9, text='Falta o ddd no telefone', width=45, font=self.fonte, fg='red')
                return self.msg.pack()

        nasc = str(self.txtdn.get()).strip()
        try:
            nasc = funcoes.inverter_datas(nasc)
        except IndexError:
            self.msg = Label(self.c9, text='Formato das datas estão invalidos',
                             width=30, font=self.fonte, fg='red')
            self.msg.pack()
            self.msg2 = Label(
                self.c9, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
            self.msg2.pack()
        else:
            try:
                query.update_cliente(codigo, nome, sobrenome, cpf, tel, email, nasc,
                                     servidor.host, servidor.usr, servidor.passwd)
            except err.InternalError:
                self.msg = Label(self.c9, text='Formato das datas estão invalidos', width=30,
                                 font=self.fonte, fg='red')
                self.msg.pack()
                self.msg2 = Label(
                    self.c9, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
                self.msg2.pack()

            except err.IntegrityError:
                self.msg = Label(self.c9, text='Este cpf já esta cadastrado', width=30,
                                 font=self.fonte, fg='red')
                self.msg.pack()

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


class BuscaExcluirCliente:

    def __init__(self):
        self.fonte = ('Verdana', '10')
        self.janela = Tk()
        self.janela.title('Clientes')
        self.janela.geometry('400x200+450+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Clientes')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbcpf = Label(self.c2, text='CPF', font=self.fonte, width=5)
        self.lbcpf.pack(side=LEFT)
        self.txtcpf = Entry(self.c2, width=30, font=self.fonte)
        self.txtcpf.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=10)
        self.busc['command'] = self.busca
        self.busc.pack()

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.msg = Label()

        self.janela.mainloop()

    def busca(self):
        from inicio import servidor
        cpf = self.txtcpf.get()
        f = funcoes.pegar_dados_clientes(cpf, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='CPF não encontrado nos registros',
                             width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            return ExcluirCliente(f['nome'], f['sobrenome'], f['cpf'], f['telefone'], f['nasc'])


class ExcluirCliente:

    def __init__(self, nome, sobrenome, cpf, telefone, nasc):
        self.janela = Tk()
        self.janela.title('Exclusão de Cliente')
        self.janela.geometry('400x300+420+200')
        self.fonte = ('Verdana', '10')
        self.cpf = cpf

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 15
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'{nome} {sobrenome}', width=30,
                            font=('Verdana', '10'))
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbnome = Label(self.c2, text='Nome', width=15, font=self.fonte)
        self.lbnome.pack(side=LEFT)
        self.nome = Label(self.c2, text=nome, width=20, font=self.fonte, bg='white')
        self.nome.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.lbsobre = Label(self.c3, text='Sobrenome', width=15, font=self.fonte)
        self.lbsobre.pack(side=LEFT)
        self.sobre = Label(self.c3, text=sobrenome, width=20, font=self.fonte, bg='white')
        self.sobre.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.lbnasc = Label(self.c4, text='Cargo', width=15, font=self.fonte)
        self.lbnasc.pack(side=LEFT)
        self.nasc = Label(self.c4, text=nasc, width=20, font=self.fonte, bg='white')
        self.nasc.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.lbtelefone = Label(self.c5, text='Admissão', width=15, font=self.fonte)
        self.lbtelefone.pack(side=LEFT)
        self.telefone = Label(self.c5, text=telefone, width=20, font=self.fonte, bg='white')
        self.telefone.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 15
        self.c6.pack()
        self.excluir = Button(self.c6, text='Excluir', width=15, font=self.fonte)
        self.excluir.pack()

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 15
        self.c7.pack()
        self.msg = Label()
        self.janela.mainloop()

    def confirma(self):
        global janela_confirmar
        janela_confirmar = Tk()
        janela_confirmar.title('Confirmação')
        janela_confirmar.geometry('250x100+520+300')
        lb = Label(janela_confirmar, text='Deseja mesmo excluir os dados?', width=30, font=self.fonte)
        lb.place(x=12, y=18)
        sim = Button(janela_confirmar, text='Sim', width=5, font=self.fonte, command=self.exclui)
        sim.place(x=78, y=50)
        nao = Button(janela_confirmar, text='Não', width=5, font=self.fonte)
        nao.place(x=128, y=50)
        janela_confirmar.mainloop()

    def exclui(self):
        janela_confirmar.destroy()
        from inicio import servidor
        query.delete_cliente(self.cpf, servidor.host, servidor.usr, servidor.passwd)
        self.janela.destroy()
        janela_sucesso = Tk()
        lb = Label(janela_sucesso, text='Dados excluidos com sucesso',
                   width=60, font=('calibru', '9', 'bold'), fg='green')
        lb.pack()
        btn = Button(janela_sucesso, text='OK', font=self.fonte, command=janela_sucesso.destroy)
        btn.pack()
        janela_sucesso.geometry('300x80+500+350')
        janela_sucesso.mainloop()
