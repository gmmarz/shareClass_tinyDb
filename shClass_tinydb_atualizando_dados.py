from tinydb import TinyDB, Query
from tinydb.table import Document

db = TinyDB('./database.json', indent=2)
t_pessoas = db.table('pessoas')

Pessoa = Query()

guilherme = db.table('pessoas').get(Pessoa.nome == 'Guilherme')
db.table('pessoas').update(
    {'altura': 1.68,'profissao':'engenheiro'},doc_ids=[guilherme.doc_id]
)

samueis = t_pessoas.search(Pessoa.nome =='Samuel')
print(samueis)
t_pessoas.remove(Pessoa.nome == 'Samuel')
samueis = t_pessoas.search(Pessoa.nome =='Samuel')
print(samueis)

