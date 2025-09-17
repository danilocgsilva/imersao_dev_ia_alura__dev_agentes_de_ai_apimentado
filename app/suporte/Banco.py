import mysql.connector
import os
from GoogleApiWrapper import GoogleApiWrapper
import pickle
import base64

class Banco:
    def __init__(self):
        self._nome_banco = None
    
    @property
    def nome_banco(self):
        return self._nome_banco
    
    @nome_banco.setter
    def nome_banco(self, nome_banco: str):
        self._nome_banco = nome_banco
        
    def executar_sql(self, sql_script: str, scaping_replacements: tuple = ()):
        try:
            mydb = mysql.connector.connect(
                host=os.environ.get("HOST_BANCO"),
                user=os.environ.get("USUARIO_BANCO"),
                password=os.environ.get("SENHA_BANCO")
            )
            mycursor = mydb.cursor()
            if self.nome_banco:
                mycursor.execute(f"USE {self.nome_banco}")
            mycursor.execute(sql_script, scaping_replacements)
            results = mycursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Error connecting to database or executing query: {err}")
        finally:
            if mydb and mydb.is_connected():
                mydb.commit()
                mycursor.close()
                mydb.close()
    
    def registrar_modelos_disponiveis(self):
        gaw = GoogleApiWrapper()
        modelos = gaw.getModels()
        modelos_serializados = pickle.dumps(modelos)
        modelos_serializados_base64 = base64.b64encode(modelos_serializados).decode('utf-8')
        self.nome_banco = os.environ.get("NOME_BANCO")
        self.executar_sql(f"INSERT INTO busca_api (comando, retorno_serializado) VALUES (%s, %s);", ('GoogleApiWrapper().getModels()', modelos_serializados_base64,))
        
        