from tkinter import *
import query
from pymysql import err
from funcoes import pegar_usuarios
import menu


def abrir_menu():
    """Função que quando invocada abrira o menu da aplicação"""
    return menu.Menu()


class Servidor:

    def __init__(self, host, usr, passwd):
        self.host = host
        self.usr = usr
        self.passwd = passwd


class Acesso:

    def __init__(self):

        self.janela = Tk()
        self.janela.title("Acesso")
        self.janela.geometry('300x250+500+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 10
        self.c1.pack()
        self.lb = Label(self.c1, width=50, font=fonte,
                        text='Acesso ao seu servidor')
        self.lb.pack()

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 7
        self.c2.pack()
        self.lblh = Label(self.c2, width=15, font=fonte, text='Host')
        self.lblh.pack(side=LEFT)
        self.localhost = Entry(self.c2, width=20, font=fonte)
        self.localhost.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 7
        self.c3.pack()
        self.lbus = Label(self.c3, width=15, font=fonte, text='User')
        self.lbus.pack(side=LEFT)
        self.user = Entry(self.c3, width=20, font=fonte)
        self.user.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 7
        self.c4.pack()
        self.lbsenha = Label(self.c4, width=15, font=fonte, text='Passwd')
        self.lbsenha.pack(side=LEFT)
        self.senha = Entry(self.c4, width=20, font=fonte)
        self.senha.pack(side=LEFT)

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 15
        self.c5.pack()
        self.conectar = Button(self.c5, width=15, text='Conectar')
        self.conectar['command'] = self.conect
        self.conectar.pack()

        self.c6 = Frame(self.janela)
        self.c6['pady'] = 10
        self.c6.pack()
        self.msg = Label()

        self.janela.mainloop()

    @property
    def host(self):
        return str(self.localhost.get()).strip()

    @property
    def usr(self):
        return str(self.user.get()).strip()

    @property
    def passwd(self):
        return str(self.senha.get()).strip()

    def pegar(self):
        global servidor
        servidor.host = str(self.localhost.get()).strip()
        servidor.usr = str(self.user.get()).strip()
        servidor.passwd = str(self.senha.get()).strip()

    def conect(self):
        self.msg.destroy()
        self.pegar()
        try:
            query.conexao(self.host, self.usr, self.passwd)
        except err.OperationalError:
            self.msg = Label(self.c6, width=50, font=fonte, text='Dados do servidor estao incorretos, verifique-os',
                             fg='red')
            return self.msg.pack()
        else:
            self.janela.destroy()
            Login()


class Login:

    def __init__(self):
        self.fonte = ('Verdana', '8')
        self.janela = Tk()
        self.janela.title('Acesso ao Sistema')
        self.janela.geometry('300x180+500+250')

        self.c1 = Frame(self.janela)
        self.c1['pady'] = 15
        self.c1.pack()
        self.titulo = Label(self.c1, text='Login', font=(
            'calibru', '16', 'bold'), width=20)
        self.titulo.pack(side=LEFT)

        self.c2 = Frame(self.janela)
        self.c2['pady'] = 5
        self.c2.pack()
        self.lbuser = Label(self.c2, text='User', width=20,
                            font=('calibru', '9', 'bold'))
        self.lbuser.pack(side=LEFT)
        self.__txtuser = Entry(
            self.c2, width=17, font=('calibru', '9', 'italic'))
        self.__txtuser.pack(side=LEFT)

        self.c3 = Frame(self.janela)
        self.c3['pady'] = 5
        self.c3.pack()
        self.lbsenha = Label(self.c3, text='Senha', width=20,
                             font=('calibru', '9', 'bold'))
        self.lbsenha.pack(side=LEFT)
        self.__txtsenha = Entry(self.c3, width=20, show='*')
        self.__txtsenha.pack(side=LEFT)

        self.c4 = Frame(self.janela)
        self.c4['pady'] = 5
        self.c4.pack()
        self.entrar = Button(self.c4, text='Entrar',
                             width=10, font=('calibru', '9', 'bold'))
        self.entrar['command'] = self.entrando
        self.entrar.pack()

        self.c5 = Frame(self.janela)
        self.c5['pady'] = 5
        self.c5.pack()

        self.msg = Label()

        self.janela.mainloop()

    @property
    def user(self):
        return str(self.__txtuser.get()).strip()

    @property
    def senha(self):
        return str(self.__txtsenha.get()).strip()

    def entrando(self):
        """Função que verifica o usuario e a senha para dar inicio a aplicação"""
        """Caso der erro de não existir o DB e as tabelas, essa função ira criar tudo que se precisa"""
        self.msg.destroy()
        try:
            usuarios = pegar_usuarios(
                servidor.host, servidor.usr, servidor.passwd)
        except err.InternalError:
            query.create_database(servidor.host, servidor.usr, servidor.passwd)
            query.create_table_users(
                servidor.host, servidor.usr, servidor.passwd)
            query.insert_user('admin', 'admin', servidor.host,
                              servidor.usr, servidor.passwd)
            # Use esses dados para login(admin) e senha(admin)
            query.create_table_produtos(
                servidor.host, servidor.usr, servidor.passwd)
            query.create_table_clientes(
                servidor.host, servidor.usr, servidor.passwd)
            query.create_table_funcionarios(
                servidor.host, servidor.usr, servidor.passwd)

            janela = Tk()
            lb = Label(janela, text='Criando o banco de dados',
                       width=60, font=('calibru', '9', 'bold'), fg='green')
            lb.pack()
            lb2 = Label(janela, text='e as tabelas para usar esse programa',
                        width=60, font=('calibru', '9', 'bold'), fg='green')
            lb2.pack()
            btn = Button(janela, text='OK', font=fonte, command=janela.destroy)
            btn.pack()
            janela.geometry('300x80+500+350')
            janela.mainloop()

        else:
            for usuario in usuarios:
                usr = self.user
                sn = self.senha
                if usr in usuario and sn == usuario[1]:
                    self.__txtsenha.delete(0, END)
                    self.__txtuser.delete(0, END)
                    self.janela.destroy()
                    return abrir_menu()

                else:
                    self.msg = Label(self.c5, text='Usuario ou senha esta incorreto', width=30,
                                     font=('calibru', '9', 'bold'), fg='red')
                    return self.msg.pack()


servidor = Servidor('', '', '')
fonte = ('calibru', '9')
