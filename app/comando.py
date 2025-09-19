import argparse
import os
from suporte.Comandos.LimparBanco import LimparBanco
from suporte.Comandos.Migrar import Migrar
from suporte.Comandos.RegistrarModelosDisponiveis import RegistrarModelosDisponiveis
from suporte.Comandos.Perguntar import Perguntar
from suporte.Comandos.RenovarBanco import RenovarBanco
import re

def clean_filename(filename):
    if not filename:
        return ""
    name_without_ext = os.path.splitext(filename)[0]
    snake_case = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name_without_ext)
    snake_case = re.sub('([A-Z])([A-Z][a-z])', r'\1_\2', snake_case)
    return {
        "comando": snake_case.lower(),
        "classe": name_without_ext
    }

def buscar_par_de_comandos():
    lista_arquivos = os.listdir("suporte/Comandos")
    lista_arquivos_comandos = [arquivo for arquivo in lista_arquivos if arquivo != "__pycache__"]
    lista_comandos_classes = list(map(lambda x: clean_filename(x), lista_arquivos_comandos))
    dict_comando_classe = {}
    for par_comando_classe in lista_comandos_classes:
        dict_comando_classe[par_comando_classe["comando"]] = par_comando_classe["classe"]
    return dict_comando_classe

def main():  
    dict_pares_comando_classe = buscar_par_de_comandos()
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--comando', 
        type=str, 
        help='Comando a ser executado',
        required=False,
        default=""
    )
    parser.add_argument(
        '--pergunta', 
        help='Pergunta ser feita',
        required=False,
        default=""
    )
    args = parser.parse_args()
    
    if args.comando in dict_pares_comando_classe or args.comando == "ajuda":
        if args.comando == "limpar_banco":
            comando = LimparBanco()
            comando.executar()
            
        if args.comando == "migrar":
            comando = Migrar()
            comando.executar()
            
        if args.comando == "registrar_modelos_disponiveis":
            comando = RegistrarModelosDisponiveis()
            comando.executar()
            
        if args.comando == "renovar_banco":
            comando = RenovarBanco()
            comando.executar()
            
        if args.comando == "perguntar":
            if args.pergunta == "":
                print("O comando para perguntar requer um segundo parâmetro, que é a --pergunta")
            else:
                perguntar = Perguntar()
                perguntar.set_pergunta(args.pergunta)
                perguntar.executar()
                resposta = perguntar.get_resposta()
                print(resposta)
            
        if args.comando == "ajuda":
            print("Comandos disponíveis:")
            for chave_comando in dict_pares_comando_classe:
                print(" * " + chave_comando)
    else:
        if args.comando == "":
            print("Você se esqueceu de dizer o comando. Utilize **python3 --comando ajuda** para ver os comandos dispníveis.")
        else:
            print(f"O comando entregue {args.comando} não existe.")

if __name__ == "__main__":
    main()