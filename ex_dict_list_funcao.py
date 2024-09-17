# Exercicio para alunos de administracao e economia
# Evento Gastronomico realizado na faculdade para arrecadar fundos para uma entidade filantrópica
#Lista dos organizadores do evento
lst_organizadores = ['bento','mariana','saulo']
# Fornecedores do evento
dict_fornecedor = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'vendas': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
}
# Clientes que consumiram no evento
list_cliente = ['rafael','douglas','amanda','jorge','jeffri','carol','cristian',
 'leonardo','maria','luana','vanessa','jose','maria','bento','mariana','saulo',
 'glauco','ze','maria', "bola"]
# Despesas do evento
locacao = 0.10 # 10% das vendas
limpeza = 700
seguranca = 800
outras_despesas = 500

# 1 - Calcular o total de vendas usando o for loop no dict
total_vendas = 0
for fornecedor in dict_fornecedor.values():
    total_vendas += fornecedor['vendas']
    vendas = fornecedor['vendas']
    nome = fornecedor['nome']
    print(f"O fornecedor é {nome} e vendeu {vendas}")
print(total_vendas)

# Os professores doaram 5000,00, cada professor doou 1000,00
# 2 - Criar um dicionario com o nome e valor
dict_professores = {
    "laerte": 5000,
    "joao gabriel": 5000,
    "glauceny": 5000,
    "zenaide": 5000,
    "taffarel": 5000
}

# 3 - Criar uma lista com os nomes dos professores
lst_professores = list(dict_professores.keys())

# 4 - Adicionar essa lista dos professores na lista de clientes
list_cliente.extend(lst_professores)

# 5 - Calcular quantas pessoas estiveram e a media de gasto por pessoa
quantidade_pessoa = len(list_cliente)
media_consumidor = total_vendas/quantidade_pessoa
print(quantidade_pessoa)
print(media_consumidor)

# 6 - Encontrar quem foi o 10 consumidor e retire da lista
list_cliente.remove(list_cliente[9])


# 7 - Encontre o nome "bola" inserido incorretamente na lista e retire da lista
list_cliente.index("bola")

if "bola" in list_cliente:
    list_cliente.remove("bola")
    print("cliente bola removido")
else:
    print("cliente bola nao encontrado")

# 8 - Verificar se todos os organizadores estao na lista
for nome in lst_organizadores:
    if nome in list_cliente:
        print(f"{nome} esta na lista!")
    else:
        print(f"{nome} NAO esta na lista!")


# 9 - Tira-los da lista
list(set(list_cliente) - set(lst_organizadores))


# 10 - fazer uma funçao que calcule o lucro liquido do evento
# entrada dos parametros sao as vendas e as despesas
# criar um pacote e gravar o modulo com essa funcao
# importe o pacote com a funcao
# chame a funcao
# execute o programa
desp_locacao = total_vendas * locacao
total_despesa = desp_locacao + limpeza + seguranca + outras_despesas

def calc_lucro_liquido(vendas, despesas):
    lucro = vendas - despesas
    return lucro

lucro_liquido = calc_lucro_liquido(total_vendas, total_despesa)
print(lucro_liquido)








