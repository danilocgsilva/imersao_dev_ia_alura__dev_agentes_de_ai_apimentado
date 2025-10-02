import argparse
import os
from suporte.Comandos.LimparBanco import LimparBanco
from suporte.Comandos.Migrar import Migrar
from suporte.Comandos.RegistrarModelosDisponiveis import RegistrarModelosDisponiveis
from suporte.Comandos.Perguntar import Perguntar
from suporte.Comandos.RenovarBanco import RenovarBanco
from suporte.Comandos.AlterarOrdemModelo import AlterarOrdemModelo
from suporte.Comandos.Rag.ListarDocumentosRag import ListarDocumentosRag
from suporte.Comandos.Rag.VerChunksDocumentos import VerChunksDocumentos
from suporte.Comandos.Rag.CarregarDocumentos import CarregarDocumentos
from suporte.Comandos.Rag.PerguntarComRag import PerguntarComRag
from suporte.Comandos.DesenharGrafo import DesenharGrafo
from suporte.Comandos.ListarPerguntasPadrao import ListarPerguntasPadrao
from suporte.Comandos.RodarAgentes import RodarAgentes
from suporte.Banco import Banco
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
    lista_arquivos += os.listdir("suporte/Comandos/Rag")
    
    exclusoes = {"__pycache__", "ComandoBase.py", "__init__.py"}
    lista_arquivos_comandos = [arquivo for arquivo in lista_arquivos if arquivo not in exclusoes ]
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
    parser.add_argument(
        '--pergunta-com-rag', 
        help='Pergunta ser feita considerando os arquivos salvos para gerar o contexto.',
        required=False,
        default=""
    )
    parser.add_argument(
        '--temperatura', 
        help='A temperatura do modelo para responder. Quanto menor, menos criativo e determinístico. Quanto maior, mais criativo e imprevisível.',
        required=False,
        default=0.1
    )
    parser.add_argument(
        '--ordem', 
        help='A ordem para ser assimilada ao modelo',
        required=False,
        default=""
    )
    parser.add_argument(
        '--modelo', 
        help='O nome do modelo',
        required=False,
        default=""
    )
    parser.add_argument(
        '--tamanho-chunk',
        help='O tamanho do chunk para o comando ver_chunks_documentos',
        required=False,
        default=300
    )
    parser.add_argument(
        '--chunk-overlap',
        help='O tamanho do overlap para o comando ver_chunks_documentos',
        required=False,
        default=30
    )
    parser.add_argument(
        '--apenas-conteudo',
        help='Se deve retornar apenas o page_content para o comando ver_chunks_documentos',
        action='store_true'
    )
    parser.add_argument(
        '--id-pergunta-padrao',
        help='O id da pergunta padrão para rodar o agente',
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
            
        if args.comando == "listar_documentos_rag":
            comando = ListarDocumentosRag()
            comando.executar()
            
        if args.comando == "carregar_documentos":
            comando = CarregarDocumentos()
            comando.executar()

        if args.comando == "ver_chunks_documentos":
            comando = VerChunksDocumentos()
            comando.executar(
                args.tamanho_chunk,
                args.chunk_overlap,
                args.apenas_conteudo
            )

        if args.comando == "listar_perguntas_padrao":
            comando = ListarPerguntasPadrao()
            comando.executar()

        if args.comando == "rodar_agentes":
            if args.id_pergunta_padrao == "":
                print("Para o comando rodar_agentes é necessário fornecer o id de uma pergunta padrão. Use o parâmetro --id-pergunta-padrao e coloque o id da pergunta padrão. Para ver as perguntas padrões disponíveis, execute o comando listar_perguntas_padrao.")
            else:
                banco = Banco()
                pergunta = banco.buscar_pergunta_padrao(int(args.id_pergunta_padrao))
                comando = RodarAgentes()
                comando.pergunta = pergunta
                comando.executar()
            
        if args.comando == "perguntar":
            if args.pergunta == "":
                print("O comando para perguntar requer um segundo parâmetro, que é a --pergunta")
            else:
                perguntar = Perguntar()
                perguntar.set_pergunta(args.pergunta)
                perguntar.set_temperatura(args.temperatura)
                perguntar.executar()
                resposta = perguntar.get_resposta()
                print(resposta)
                
        if args.comando == "perguntar_com_rag":
            if args.pergunta == "":
                print("O comando para perguntar requer um segundo parâmetro, que é a --pergunta")
            else:
                perguntar = PerguntarComRag()
                perguntar.set_pergunta(args.pergunta)
                perguntar.executar()
                resposta = perguntar.get_resposta()
                if args.apenas_conteudo:
                    print(resposta["answer"])
                else:
                    print(resposta)
                
        if args.comando == "alterar_ordem_modelo":
            if args.modelo == "" or args.ordem == "":
                print("O comando para alterar a ordem do modelo requer dois parâmetros, que são --modelo e --ordem")
            else:
                alterarOrdemModelo = AlterarOrdemModelo()
                alterarOrdemModelo.modelo = args.modelo
                alterarOrdemModelo.ordem = args.ordem
                alterarOrdemModelo.executar()
                
        if args.comando == "desenhar_grafo":
            comando = DesenharGrafo()
            comando.executar()
            
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