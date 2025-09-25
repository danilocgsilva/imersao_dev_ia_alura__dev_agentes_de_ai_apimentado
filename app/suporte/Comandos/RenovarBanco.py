from suporte.Comandos.LimparBanco import LimparBanco
from suporte.Comandos.Migrar import Migrar
from suporte.Comandos.ComandoBase import ComandoBase

class RenovarBanco(ComandoBase):
    def executar(self):
        LimparBanco().executar()
        Migrar().executar()
