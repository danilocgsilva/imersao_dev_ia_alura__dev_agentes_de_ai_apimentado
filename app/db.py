import mysql.connector
import os

def sql(query_string: str):
    mydb = mysql.connector.connect(
        host=os.environ.get("HOST_BANCO"),
        user=os.environ.get("USUARIO_BANCO"),
        password=os.environ.get("SENHA_BANCO")
    )
    
    mycursor = mydb.cursor()

    results = mycursor.execute(query_string)
    
    
sql("CREATE DATABASE imersao_alura_dev_agentes_ia;")    
    