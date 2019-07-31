#conexão com banco de dados:
import MySQLdb

host = "127.0.0.1"
user = "oficina_bike"
password = "123456"
db = "oficina_bike"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)
#cursor: utilizada para pegar como resultado no select
#executar consultas
# DictCursors faz com que "c" retorne uma lista de dicionários

#------------------------------SELECT-------------------------------
# SELECT atributos FROM tabela WHERE condição
def select(fields, tables, where=None):
	global c

	query = "SELECT " + fields + " FROM " + tables
	if where:
		query = query + " WHERE " + where

	c.execute(query)
	return c.fetchall()
	#fechall pega todos os resultados do execute e retorna


#------------------------------------INSERT-------------------------
# INSERT INTO tabela (atributos) VALUES (registros)
# INSERT INTO tabela VALUES (registros)
def insert(values, table, fields=None):
	#no caso do insert, tanto o cursor como a conexão são
	#necessários, para fazer o commit
	global c, con

	query = "INSERT INTO " + table
	if fields:
		query = query + " (" + fields + ") "

	# O join vai pegar todos os elementos da lista values, 'encapsulando' cada um
	# com parênteses e separando-os por vírgula
	query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

	c.execute(query)
	con.commit()

#-----------------------------update-------------------------
# UPDATE tabela SET atributo = 'valor'
#sets = diconário onde a key = atributo, valor = value
def update(sets, table, where=None):
	global c, con
	query = "UPDATE " + table
	query = query + " SET " + ",".join([field + " = '" +  value + "'" for field, value in sets.items()])
	if where:
		query = query + " WHERE " + where

	c.execute(query)
	con.commit()

#-----------------------------delete---------------------------------
# DELETE FROM tabela WHERE condição
def delete(table, where):
	global c, con

	query = "DELETE FROM " + table + " WHERE " + where

	c.execute(query)
	con.commit()