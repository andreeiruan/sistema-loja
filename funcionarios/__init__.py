from tkinter import *
import funcoes
import query
from pymysql import err


def alterar():
    return BuscarFuncionarioAlterar()


def adicionar():
    return InserirFuncionario()


def buscar():
    return BuscarFuncionario()


def excluir():
    return BuscarFuncionarioExcluir()


janela_confirmar = None


class Funcionarios:

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Funcionarios')
        self.janela.geometry('400x350+450+200')

        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Funcionários')
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


class BuscarFuncionario:

    def __init__(self):
        self.fonte = ('Verdana', '10')
        self.janela = Tk()
        self.janela.title('Funcionarios')
        self.janela.geometry('400x200+450+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Funcionario')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack(side=LEFT)

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
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=15)
        self.busc['command'] = self.busca
        self.busc.pack(side=RIGHT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.msg = Label()

    def busca(self):
        from inicio import servidor
        self.msg.destroy()
        codigo = str(self.txtcpf.get()).strip()
        f = funcoes.pegar_dados_funcionario(codigo, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='CPF não encontrado nos registros', width=30, font=self.fonte,
                             fg='red')
            return self.msg.pack()

        else:
            return ResultadoBuscaFuncionario(f['id'], f['nome'], f['sobrenome'], f['cpf'], f['cargo'], f['telefone'],
                                             f['email'], f['admissao'], f['nasc'])


class ResultadoBuscaFuncionario:

    def __init__(self, codigo, nome, sobrenome, cpf, cargo, telefone, email, admissao, nasc):

        self.janela = Tk()
        self.janela.title(f"Dados do Funcionario {nome}")
        self.janela.geometry('500x500+400+100')
        self.fonte = ('Verdana', '10')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text=f'{nome} {sobrenome}')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbid = Label(self.c2, text='ID', font=self.fonte, width=30)
        self.lbid.pack(side=LEFT)
        self.txtid = Label(self.c2, text=codigo, font=self.fonte, width=30)
        self.txtid.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.lbnome = Label(self.c3, text='Nome', font=self.fonte, width=30)
        self.lbnome.pack(side=LEFT)
        self.txtnome = Label(self.c3, text=nome, font=self.fonte, width=30, bg='white')
        self.txtnome.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.lbsobrenome = Label(self.c4, text='Sobrenome', font=self.fonte, width=30)
        self.lbsobrenome.pack(side=LEFT)
        self.txtsobrenome = Label(self.c4, text=sobrenome, font=self.fonte, width=30, bg='white')
        self.txtsobrenome.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.lbcpf = Label(self.c5, text='CPF', font=self.fonte, width=30)
        self.lbcpf.pack(side=LEFT)
        self.txtcpf = Label(self.c5, text=cpf, font=self.fonte, width=30, bg='white')
        self.txtcpf.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 7
        self.c6.pack()
        self.lbcargo = Label(self.c6, text='Cargo', font=self.fonte, width=30)
        self.lbcargo.pack(side=LEFT)
        self.txtcargo = Label(self.c6, text=cargo, font=self.fonte, width=30, bg='white')
        self.txtcargo.pack(side=LEFT)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 7
        self.c7.pack()
        self.lbtel = Label(self.c7, text='Telefone', font=self.fonte, width=30)
        self.lbtel.pack(side=LEFT)
        self.txttel = Label(self.c7, text=telefone, font=self.fonte, width=30, bg='white')
        self.txttel.pack(side=LEFT)

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 7
        self.c8.pack()
        self.lbemail = Label(self.c8, text='Email', font=self.fonte, width=30)
        self.lbemail.pack(side=LEFT)
        self.txtemail = Label(self.c8, text=email, font=self.fonte, width=30, bg='white')
        self.txtemail.pack(side=LEFT)

        self.c9 = Frame(self.janela)
        self.c9['pady'] = 7
        self.c9.pack()
        self.lbad = Label(self.c9, text='Admissao', font=self.fonte, width=30)
        self.lbad.pack(side=LEFT)
        self.txtad = Label(self.c9, text=admissao, font=self.fonte, width=30, bg='white')
        self.txtad.pack(side=LEFT)

        self.c10 = Frame(self.janela)
        self.c10['pady'] = 7
        self.c10.pack()
        self.lbdn = Label(self.c10, text='Data de Nascimento', font=self.fonte, width=30)
        self.lbdn.pack(side=LEFT)
        self.txtdn = Label(self.c10, text=nasc, font=self.fonte, width=30, bg='white')
        self.txtdn.pack(side=LEFT)

        self.janela.mainloop()


class InserirFuncionario:

    def __init__(self):
        self.fonte = ('Verdana', '10')
        self.janela = Tk()
        self.janela.title('Casdastrar funcionario')
        self.janela.geometry('500x500+400+100')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 15
        self.c1.pack()
        self.titulo = Label(self.c1, text='Cadastrar Funcionario', width=25)
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack(side=LEFT)

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lbnome = Label(self.c2, text='Nome', font=self.fonte, width=20)
        self.lbnome.pack(side=LEFT)
        self.txtnome = Entry(self.c2, width=30, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.lbsobre = Label(self.c3, text='Sobrenome', font=self.fonte, width=20)
        self.lbsobre.pack(side=LEFT)
        self.txtsobre = Entry(self.c3, width=30, font=self.fonte)
        self.txtsobre.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.lbcpf = Label(self.c4, text='CPF', font=self.fonte, width=20)
        self.lbcpf.pack(side=LEFT)
        self.txtcpf = Entry(self.c4, width=30, font=self.fonte)
        self.txtcpf.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.lbcargo = Label(self.c5, text='Cargo', font=self.fonte, width=20)
        self.lbcargo.pack(side=LEFT)
        self.txtcargo = Entry(self.c5, width=30, font=self.fonte)
        self.txtcargo.pack(side=LEFT)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 7
        self.c6.pack()
        self.lbtel = Label(self.c6, text='Telefone', font=self.fonte, width=20)
        self.lbtel.pack(side=LEFT)
        self.txttel = Entry(self.c6, width=30, font=self.fonte)
        self.txttel.pack(side=LEFT)

        self.c7 = Frame(self.janela)
        self.c7['pady'] = 7
        self.c7.pack()
        self.lbemail = Label(self.c7, text='Email', font=self.fonte, width=20)
        self.lbemail.pack(side=LEFT)
        self.txtemail = Entry(self.c7, width=30, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.c8 = Frame(self.janela)
        self.c8['pady'] = 7
        self.c8.pack()
        self.lbad = Label(self.c8, text='Admissão', font=self.fonte, width=20)
        self.lbad.pack(side=LEFT)
        self.txtad = Entry(self.c8, width=30, font=self.fonte)
        self.txtad.pack(side=LEFT)

        self.c9 = Frame(self.janela)
        self.c9['pady'] = 7
        self.c9.pack()
        self.lbnasc = Label(self.c9, text='Data de Nascimento', font=self.fonte, width=20)
        self.lbnasc.pack(side=LEFT)
        self.txtnasc = Entry(self.c9, width=30, font=self.fonte)
        self.txtnasc.pack(side=LEFT)

        self.c10 = Frame(self.janela)
        self.c10['pady'] = 20
        self.c10.pack()
        self.btninserir = Button(self.c10, text='Inserir', font=self.fonte, width=20)
        self.btninserir['command'] = self.inserir
        self.btninserir.pack()

        self.c11 = Frame(self.janela)
        self.c11['pady'] = 5
        self.c11.pack()

        self.msg = Label()
        self.msg2 = Label()

        self.janela.mainloop()

    def inserir(self):
        """Função que faz o tratamento dos dados que serão inseridos na tabela,
                se tiver algum problema ela retornara avisando
                se tiver tudo ok, os dados serão inseridos na tabela"""
        from inicio import servidor
        self.msg.destroy()
        self.msg2.destroy()

        nome = str(self.txtnome.get()).title().strip()
        if len(nome) == 0:
            self.msg = Label(self.c11, text='Campo nome esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        sobrenome = str(self.txtsobre.get()).title().strip()
        if len(sobrenome) == 0:
            self.msg = Label(self.c11, text='Campo sobrenome esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        cpf = str(self.txtcpf.get()).title().strip().replace('-', '')
        if len(cpf) != 11:
            self.msg = Label(self.c11, text='CPF esta de forma incorreta!', width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            for n in cpf:
                if not n.isnumeric():
                    self.msg = Label(self.c11, text='CPF esta de forma incorreta!', width=30, font=self.fonte, fg='red')
                    return self.msg.pack()

        cargo = str(self.txtcargo.get()).title().strip()
        if len(cargo) == 0:
            self.msg = Label(self.c11, text='Campo cargo esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        telefone = str(self.txttel.get()).title().strip().replace(' ', '')
        if len(telefone) != 11:
            self.msg = Label(self.c11, text='Telefone esta de forma incorreta', width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            for n in telefone:
                if not n.isnumeric():
                    self.msg = Label(self.c11, text='Telefone esta de forma incorreta',
                                     width=30, font=self.fonte, fg='red')
                    return self.msg.pack()

            if telefone[0] != '5' and telefone[1] != '1':
                self.msg = Label(self.c11, text='Falta o DDD no telefone', width=30, font=self.fonte, fg='red')
                return self.msg.pack()

        email = str(self.txtemail.get()).title().strip()
        if len(email) == 0:
            self.msg = Label(self.c11, text='Campo email esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        admissao = str(self.txtad.get()).title().strip()
        nasc = str(self.txtnasc.get()).title().strip()
        try:
            admissao = funcoes.inverter_datas(admissao)
            nasc = funcoes.inverter_datas(nasc)
        except IndexError:
            self.msg = Label(self.c11, text='Formato das datas estão invalidos', width=30, font=self.fonte, fg='red')
            self.msg.pack()
            self.msg2 = Label(self.c11, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
            self.msg2.pack()
        else:
            try:
                query.insert_funcionario(nome, sobrenome, cpf, cargo, telefone, email, admissao,
                                         nasc, servidor.host, servidor.usr, servidor.passwd)
            except err.InternalError:
                self.msg = Label(self.c11, text='Formato das datas estão invalidos', width=30,
                                 font=self.fonte, fg='red')
                self.msg.pack()
                self.msg2 = Label(self.c11, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
                self.msg2.pack()

            except err.IntegrityError:
                self.msg = Label(self.c11, text='Este cpf já esta cadastrado', width=30,
                                 font=self.fonte, fg='red')
                self.msg.pack()

            else:
                self.msg2 = Label(self.c11, text='Dados inseridos com sucesso', width=30, font=self.fonte, fg='green')
                self.msg2.pack()
                self.txtnome.delete(0, END)
                self.txtsobre.delete(0, END)
                self.txtcpf.delete(0, END)
                self.txtcargo.delete(0, END)
                self.txttel.delete(0, END)
                self.txtemail.delete(0, END)
                self.txtad.delete(0, END)
                self.txtnasc.delete(0, END)


class BuscarFuncionarioAlterar:
    def __init__(self):
        self.fonte = ('Verdana', '10')
        self.janela = Tk()
        self.janela.title('Funcionarios')
        self.janela.geometry('400x200+450+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Funcionario')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack(side=LEFT)

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
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=15)
        self.busc['command'] = self.busca
        self.busc.pack(side=RIGHT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.msg = Label()

    def busca(self):
        from inicio import servidor
        self.msg.destroy()
        codigo = str(self.txtcpf.get()).strip()
        f = funcoes.pegar_dados_funcionario(codigo, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='CPF não encontrado nos registros', width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            return AlterarFuncionario(f['id'], f['nome'], f['sobrenome'], f['cpf'], f['cargo'], f['telefone'],
                                      f['email'], f['admissao'], f['nasc'])


class AlterarFuncionario:

    def __init__(self, codigo, nome, sobrenome, cpf, cargo, telefone, email, admissao, nasc):
        self.janela = Tk()
        self.janela.title(f"Dados do Funcionario {nome}")
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
        self.lbcargo = Label(self.c5, text='Cargo', font=self.fonte, width=30)
        self.lbcargo.pack(side=LEFT)
        self.txtcargo = Entry(self.c5, font=self.fonte, width=30)
        self.txtcargo.pack(side=LEFT)
        self.txtcargo.insert(INSERT, cargo)

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 7
        self.c6.pack()
        self.lbtel = Label(self.c6, text='Telefone', font=self.fonte, width=30)
        self.lbtel.pack(side=LEFT)
        self.txttel = Entry(self.c6, font=self.fonte, width=30)
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
        self.lbad = Label(self.c8, text='Admissao', font=self.fonte, width=30)
        self.lbad.pack(side=LEFT)
        self.txtad = Entry(self.c8, font=self.fonte, width=30)
        self.txtad.pack(side=LEFT)
        self.txtad.insert(INSERT, admissao)

        self.c9 = Frame(self.janela)
        self.c9['pady'] = 7
        self.c9.pack()
        self.lbdn = Label(self.c9, text='Data de Nascimento', font=self.fonte, width=30)
        self.lbdn.pack(side=LEFT)
        self.txtdn = Entry(self.c9, font=self.fonte, width=30)
        self.txtdn.pack(side=LEFT)
        self.txtdn.insert(INSERT, nasc)

        self.c10 = Frame(self.janela)
        self.c10['pady'] = 20
        self.c10.pack()
        self.alterar = Button(self.c10, text='Alterar', font=self.fonte, width=20)
        self.alterar['command'] = self.update
        self.alterar.pack()

        self.c11 = Frame(self.janela)
        self.c11['pady'] = 7
        self.c11.pack()
        self.msg = Label()

        self.c12 = Frame(self.janela)
        self.c12['pady'] = 7
        self.c12.pack()
        self.msg2 = Label()

        self.janela.mainloop()

    def update(self):
        from inicio import servidor
        self.msg.destroy()
        self.msg2.destroy()

        cod = self.codigo

        n = str(self.txtnome.get()).title().strip()
        if len(n) == 0:
            self.msg = Label(self.c11, text='Campo nome esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        s = str(self.txtsobrenome.get()).title().strip()
        if len(s) == 0:
            self.msg = Label(self.c11, text='Campo sobrenome esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        cp = str(self.txtcpf.get()).title().strip().replace(' ', '')
        if len(cp) != 11 and not str(cp).isnumeric():
            self.msg = Label(self.c11, text='CPF esta de forma incorreta!', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        car = str(self.txtcargo.get()).title().strip()
        if len(car) == 0:
            self.msg = Label(self.c11, text='Campo cargo esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        tel = str(self.txttel.get()).title().strip().replace(' ', '')
        if len(tel) != 11:
            self.msg = Label(self.c11, text='Telefone esta de forma incorreta', width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            if tel[0] != '5' and tel[1] != '1':
                self.msg = Label(self.c11, text='Falta o DDD no telefone', width=30, font=self.fonte, fg='red')
                return self.msg.pack()

        em = str(self.txtemail.get()).title().strip()
        if len(em) == 0:
            self.msg = Label(self.c11, text='Campo email esta vazio', width=30, font=self.fonte, fg='red')
            return self.msg.pack()

        ad = str(self.txtad.get()).title().strip()
        nas = str(self.txtdn.get()).title().strip()
        try:
            ad = funcoes.inverter_datas(ad)
            nas = funcoes.inverter_datas(nas)
        except IndexError:
            self.msg = Label(self.c11, text='Formato das datas estão invalidos', width=30, font=self.fonte, fg='red')
            self.msg.pack()
            self.msg2 = Label(self.c11, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
            self.msg2.pack()
        else:
            try:
                query.update_funcionario(cod, n, s, cp, car, tel, em, ad, nas,
                                         servidor.host, servidor.usr, servidor.passwd)

            except err.InternalError:
                self.msg = Label(self.c11, text='Formato das datas estão invalidos', width=30,
                                 font=self.fonte, fg='red')
                self.msg.pack()
                self.msg2 = Label(self.c11, text='Modelo correto: (DD/MM/AAAA)', width=30, font=self.fonte, fg='red')
                self.msg2.pack()

            except err.IntegrityError:
                self.msg = Label(self.c11, text='Este cpf já esta cadastrado', width=30,
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


class BuscarFuncionarioExcluir:

    def __init__(self):
        self.fonte = ('Verdana', '10')
        self.janela = Tk()
        self.janela.title('Funcionarios')
        self.janela.geometry('400x200+450+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 30
        self.c1.pack()
        self.titulo = Label(self.c1, text='Funcionario')
        self.titulo['font'] = ('calibru', '16', 'bold')
        self.titulo.pack(side=LEFT)

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
        self.busc = Button(self.c3, text='Buscar', font=self.fonte, width=15)
        self.busc['command'] = self.busca
        self.busc.pack(side=RIGHT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.msg = Label()

    def busca(self):
        from inicio import servidor
        self.msg.destroy()
        codigo = str(self.txtcpf.get()).strip()
        f = funcoes.pegar_dados_funcionario(codigo, servidor.host, servidor.usr, servidor.passwd)
        if len(f) == 0:
            self.msg = Label(self.c4, text='CPF não encontrado nos registros', width=30, font=self.fonte, fg='red')
            return self.msg.pack()
        else:
            return ExcluirFuncionario(f['cpf'], f['nome'], f['sobrenome'], f['cargo'], f['admissao'])


class ExcluirFuncionario:

    def __init__(self, cpf, nome, sobrenome, cargo, admissao):
        self.janela = Tk()
        self.janela.title('Exclusão de Funcionario')
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
        self.lbcargo = Label(self.c4, text='Cargo', width=15, font=self.fonte)
        self.lbcargo.pack(side=LEFT)
        self.cargo = Label(self.c4, text=cargo, width=20, font=self.fonte, bg='white')
        self.cargo.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 7
        self.c5.pack()
        self.lbadmissao = Label(self.c5, text='Admissão', width=15, font=self.fonte)
        self.lbadmissao.pack(side=LEFT)
        self.admissao = Label(self.c5, text=admissao, width=20, font=self.fonte, bg='white')
        self.admissao.pack(side=LEFT)

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
        query.delete_funcionario(self.cpf, servidor.host, servidor.usr, servidor.passwd)
        self.janela.destroy()
        janela_sucesso = Tk()
        lb = Label(janela_sucesso, text='Dados excluidos com sucesso',
                   width=60, font=('calibru', '9', 'bold'), fg='green')
        lb.pack()
        btn = Button(janela_sucesso, text='OK', font=self.fonte, command=janela_sucesso.destroy)
        btn.pack()
        janela_sucesso.geometry('300x80+500+350')
        janela_sucesso.mainloop()
