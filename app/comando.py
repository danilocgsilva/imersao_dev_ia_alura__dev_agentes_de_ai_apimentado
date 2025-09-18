import argparse
import os
from suporte.Comandos.LimparBanco import LimparBanco
from suporte.Comandos.Migrar import Migrar
from suporte.Comandos.RegistrarModelosDisponiveis import RegistrarModelosDisponiveis

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--comando', type=str, help='Comando a ser executado')
    
    args = parser.parse_args()

    if args.comando == "limpar_banco":
        LimparBanco().executar()
        
    if args.comando == "migrar":
        Migrar().executar()
        
    if args.comando == "registrar_modelos_disponiveis":
        RegistrarModelosDisponiveis().execute()

if __name__ == "__main__":
    main()