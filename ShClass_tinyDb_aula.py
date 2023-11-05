#Inicio da aula
from tinydb import TinyDB

#Para criar o banco de dados.
db = TinyDB('./databse.json', indent = 2)

#Criando um documento 
document = {'name':'Davi','altura':1.75}

#Inserir informações no banco
db.insert(document)

