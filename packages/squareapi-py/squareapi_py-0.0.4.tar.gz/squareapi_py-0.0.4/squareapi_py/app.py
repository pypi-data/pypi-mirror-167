# squarecloud unofficial API module

#=================================== Imports ======================================#

import colorama
from colorama import Fore
colorama.init(autoreset=True)

from . import connection_API
#================================== Variaveis ======================================#

url_base = 'https://api.squarecloud.app/v1/public/'
#===================================================================================#

"""
    modulo que faz todas as requisições para API da squarecloud com funções. 
    ==========================================================================
    criador: Astro // discord-tag: #Astro.#0176
    data-de-modificação: 17/09/2022
"""

class Client():
    def __init__(self, 
                 key_api, 
                 id_app
                 ): 
        
        """
            classe Client que recolher os paramentros necessarios para que a lib funcione corretamente
            
                * key_api
                * id_app
        """
        
        self.key_api = key_api
        self.id_app = id_app
        
#Funções Post --> [status/ status_format/ logs/ logs_complete/ backup]
       
    def status(self):
        """
            função [status] ela faz uma requisição com o metado GET e a API retorna um dicionario json com os status do bot indicado.
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return: --> {dic-json}
        """
        
        url = f'{url_base}status/{self.id_app}'
        response = connection_API.square_connection(url=url, key_api= self.key_api)
    
        return response.R_GET()
    
    def status_format(self):
        """
            função [status_format] ela pega da função [status] o dicionario json e formata.
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return --> status formatado
        """
        
        response_json = self.status()
        status_dic = response_json['response']
        return_formt = f'Status: {status_dic["status"]}\nCpu: {status_dic["cpu"]}\nMemória: {status_dic["ram"]}\nSSD: {status_dic["storage"]}\nNetwork: {status_dic["network"]}\nRequests: {status_dic["requests"]}/200'

        return return_formt
    
    def logs(self):
        """
            função [logs] que faz uma requisição a API com o metado GET para puxar as ultimas 5 logs da aplicação
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return --> logs ja formatada
        """
        
        url = f'{url_base}logs/{self.id_app}'
        response = connection_API.square_connection(url=url, key_api= self.key_api)

        return response.R_GET()['response']['logs']
    
    def logs_complete(self):
        """
            função [logs_complete] faz uma requisição a API com o metado GET para puxar todas as logs da aplicação hospedada na squarecloud
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return --> link para o site da squarecloud
        """
        
        url = f'{url_base}logs-complete/{self.id_app}'
        response = connection_API.square_connection(url=url, key_api= self.key_api)
        
        return response.R_GET()["response"]["logs"]
    
    def backup(self):
        """
            função [backup] faz uma requisição a API com o metado GET para puxar um backup da aplicação
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return --> link para o site da squarecloud
        """
        
        url = f'{url_base}backup/{self.id_app}'
        response = connection_API.square_connection(url=url, key_api= self.key_api)
        
        return response.R_GET()["response"]["downloadURL"]
    
#Funções Post --> [start/ stop/ restart]

    def start(self):
        """
            função [logs_complete] enviar uma requisição para API com o metado POST para ligar a aplicação
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return --> msg de sucesso
        """
        
        url = f'{url_base}start/{self.id_app}'
        response = connection_API.square_connection(url=url, key_api= self.key_api)
        
        if self.status()['response']['status'] == 'running': return Fore.RED + 'Um erro inesperado aconteceu:\nERROR: O bot ja está ligado'
        
        response.R_POST()
        
        return Fore.YELLOW + 'Your bot has been started.'
    
    def stop(self):
        """
            função [logs_complete] enviar uma requisição para API com o metado POST para desligar a aplicação
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return --> msg de sucesso
        """
        
        url = f'{url_base}stop/{self.id_app}'
        response = connection_API.square_connection(url=url, key_api= self.key_api)
        
        if self.status()['response']['status'] == 'exited': return Fore.RED + 'Um erro inesperado aconteceu:\nERROR: O bot ja está parado'
        
        response.R_POST()
        
        return Fore.YELLOW + 'your bot has been stopped.'
    
    def restart(self):
        """
            função [logs_complete] enviar uma requisição para API com o metado POST para reiniciar a aplicação
            
            parametros necessarios: [key_api, id_app]
            
                * key_api --> chave da API 
                * id_app ==> id do bot que deseja coletar as informações
                
            return --> msg de sucesso
        """
        
        url = f'{url_base}stop/{self.id_app}'
        response = connection_API.square_connection(url=url, key_api= self.key_api)
        response.R_POST()
        
        return Fore.YELLOW + 'your bot has been restarted'