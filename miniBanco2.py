#Inicio da aula
from tinydb import TinyDB

#Para criar o banco de dados.
db = TinyDB('./databse.json', indent = 2)

#Inserir informações no banco
db.table('pessoas').insert({
    'nome':'Walter',
    'altura': 1.80})

db.table('animais').insert({
    'animal':'gato',
    'cor':'laranja',
    'demon':True
})