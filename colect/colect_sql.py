import pymysql
import pandas as pd
from sqlalchemy import create_engine

def conexao_mysql(host, user, password, db, table):
    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    
    cursor = conn.cursor()
    
    query = 'SELECT * FROM ' + table + ' limit 10'
    cursor.execute(query)
    
    resultados = cursor.fetchall()
    
    print('Tabela MySQL: ')
    for linha in resultados:
        print(linha)
        
    cursor.close()
    conn.close()
    
#conexao_mysql('localhost', 'root', '#12Stones', 'restaurante', 'clientes')

def df_conexao_mysql(host, user, password, db, table):
   
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)
    
    query = 'SELECT * FROM ' + table
    df = pd.read_sql(query, conn)
    
    print('Tabela Mysql com DataFrame : \n', df.head())
    
    conn.dispose()
    return df

df_cliente = df_conexao_mysql('localhost', 'root', '#12Stones', 'restaurante', 'clientes')
df_cliente.to_excel('dados.xlsx', index=False)

