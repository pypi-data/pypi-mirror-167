# squarecloud unofficial API module

#=================================== Imports ======================================#

import colorama
from colorama import Fore
colorama.init(autoreset=True)
#===================================================================================#

"""
    modulo que contem as funções que trata os erros das funções do modulo [app]
    ===========================================================================
    * tratar_error --> trata todos os erros da função principal
"""


class error():
    def __init__(self, error):
        self.teste = error
        
    def tratar_erro(self):
        if self.teste == 'APP_NOT_FOUND':
            return str(Fore.RED + "Ocorreu um erro inesperado\nError: A aplicação indicada não foi achada")
        
        if self.teste == 'ACCESS_DENIED':
            return str(Fore.RED + "Ocorreu um erro inesperado\nError: Sua requisição na api foi negada")