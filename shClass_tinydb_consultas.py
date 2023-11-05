from tinydb import TinyDB, Query

def mostrar_pessoas(pessoas: list[dict]):
    for index, pessoa in enumerate(pessoas, start=1):
        print(f'------ {index}º -----')
        print(f'Nome: {pessoa["nome"]}')
        print(f'Altura: {pessoa["altura"]}')
        print(f'Profissão: {pessoa["profissao"]}')
        print('----------------')

db = TinyDB('./database.json', indent=2)
t_pessoas = db.table('pessoas')

# #pesquisando todas as pessoas
# pessoas = t_pessoas.all
# mostrar_pessoas(pessoas)

pessoa = Query()

pessoas = t_pessoas.search(pessoa.altura < 1.65)
# mostrar_pessoas(pessoas)
desenvolvedores = t_pessoas.search(pessoa.profissao=='Desenvolvedor')

#Mostrando pessoas que tenham s no nome
pessoas_com_s = t_pessoas.search(pessoa.nome.search('s'))
# mostrar_pessoas(pessoas_com_s)


