from tinydb import TinyDB

db = TinyDB('./database2.json', indent=2)
table_produtos = db.table('produtos') # podemos atribuir a tabela a uma variavel

pproduto1 = {'nome':'Notebook','preco':3999.90,'processador':'intel core i5','ram_gb':8}
pproduto2 = {'nome':'geladeira','preco':4500.90,'volume_litros':300,'dispenser_agua':False}

db.table('produtos').insert(pproduto1) #Podemos inserir acessando a tabela diretamente
table_produtos.insert(pproduto2) # ou podemos inserir atraves da varial da tabela