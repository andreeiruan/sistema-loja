def formatar_datas(data):
    data = data.split('-')
    data_formatada = f'{data[2]}/{data[1]}/{data[0]}'
    return data_formatada


def inverter_datas(data):
    data = data.split(data[2])
    data = f'{data[2]}-{data[1]}-{data[0]}'
    return data


def pegar_dados_funcionario(cpf, h, u, s):
    from query import get_funcionario
    funcionario = dict()
    dados = (dado for dado in get_funcionario(cpf, h, u, s))
    for dado in dados:
        for i, d in enumerate(dado):
            if i == 0:
                funcionario['id'] = d
                continue
            if i == 1:
                funcionario['nome'] = d.title()
                continue
            if i == 2:
                funcionario['sobrenome'] = d.title()
                continue
            if i == 3:
                funcionario['cpf'] = d
                continue
            if i == 4:
                funcionario['cargo'] = d.title()
                continue
            if i == 5:
                funcionario['telefone'] = d
                continue
            if i == 6:
                funcionario['email'] = d
                continue
            if i == 7:
                funcionario['admissao'] = formatar_datas(d)
                continue
            if i == 8:
                funcionario['nasc'] = formatar_datas(d)
    return funcionario


def pegar_dados_clientes(cpf, h, u, s):
    from query import get_cliente
    cliente = dict()
    dados = (dado for dado in get_cliente(cpf, h, u, s))
    for dado in dados:
        for i, d in enumerate(dado):
            if i == 0:
                cliente['id'] = d
                continue
            if i == 1:
                cliente['nome'] = d.title()
                continue
            if i == 2:
                cliente['sobrenome'] = d.title()
                continue
            if i == 3:
                cliente['cpf'] = d
                continue
            if i == 4:
                cliente['email'] = d
                continue
            if i == 5:
                cliente['telefone'] = d
                continue
            if i == 6:
                cliente['nasc'] = formatar_datas(d)
    return cliente


def pegar_dados_produto(codigo, h, u, s):
    from query import get_produto
    produto = dict()
    dados = (dado for dado in get_produto(codigo, h, u, s))
    for dado in dados:
        for i, d in enumerate(dado):
            if i == 0:
                produto['codigo'] = d
                continue
            if i == 1:
                produto['nome'] = d.title()
                continue
            if i == 2:
                produto['marca'] = d.title()
                continue
            if i == 3:
                produto['preco'] = f"R${d.replace('.', ',')}"
                continue
            if i == 4:
                produto['descricao'] = d
                continue
            if i == 5:
                produto['estoque'] = d
    return produto


def pegar_usuarios(h, u, s):
    from query import get_users
    dados = (dado for dado in get_users(h, u, s))
    return list(dados)
