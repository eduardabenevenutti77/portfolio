from mysql.connector import connect

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

connection = mysql_connection('localhost', 'root', '', 'revisao')

query = '''
    create database teste
'''
cursor = connection.cursor()
cursor.execute(query)

connection.close()

connection = mysql_connection('localhost', 'root', '', 'revisao', 'teste')

query = '''
    create table clientes(
        id int primary key,
        nome varchar(100),
        telefone varchar(15),
        email varchar(100),
        cidade varchar(50)
    )
'''
cursor = connection.cursor()
cursor.execute(query)

query = '''
    INSERT INTO clientes VALUES
        (1001, 'Joãozinho Silva', '7199999-9999', 'joao@email.com', 'Salvador'),
        (1002, 'Paula Silva', '2199999-9999', 'paula@email.com', 'Rio'),
        (1003, 'Patricia Silva', '1199999-9999', 'paty@email.com', 'Sampa'),
        (1004, 'Zé Silva', '4199999-9999', 'ze@email.com', 'Curitiba'),
        (1005, 'Richarlison Pombo', '3199999-9999', 'pombo@email.com', 'Nova Venécia'),
        (1006, 'Vini Junior', '2199999-9999', 'vini@email.com', 'Rio'),
        (1007, 'Neymar Junior', '1199999-9999', 'ney@email.com', 'Santos')
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()

query = '''
    SELECT * FROM clientes
'''
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()
for row in result:
  print(row)