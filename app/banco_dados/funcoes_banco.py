import mysql.connector
import os

def executar_sql(query_string: str):
    try:
        mydb = mysql.connector.connect(
            host=os.environ.get("HOST_BANCO"),
            user=os.environ.get("USUARIO_BANCO"),
            password=os.environ.get("SENHA_BANCO")
        )
        mycursor = mydb.cursor()
        mycursor.execute(query_string)
        results = mycursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(f"Error connecting to database or executing query: {err}")
    finally:
        if mydb and mydb.is_connected():
            mycursor.close()
            mydb.close()
