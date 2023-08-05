import colorama
from colorama import Fore
colorama.init(autoreset=True)

class error():
    def __init__(self, error):
        self.teste = error
        
    def tratar_erro(self):
        if self.teste == 'APP_NOT_FOUND':
            return str(Fore.RED + "Ocorreu um erro inesperado\nError: A aplicação indicada não foi achada")
        
        if self.teste == 'ACCESS_DENIED':
            return str(Fore.RED + "Ocorreu um erro inesperado\nError: Sua requisição na api foi negada")