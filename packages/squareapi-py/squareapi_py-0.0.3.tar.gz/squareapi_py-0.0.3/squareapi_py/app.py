# modulo não oficial que ultilizar a api da squarecloud

import requests
import colorama
from colorama import Fore
import threading
import time
import json
colorama.init(autoreset=True)

from . import square_erro

class Client():
    def __init__(self, key_api, id_app):
        
        self.key_api = key_api
        self.id_app = id_app

# Requests GET: --> [status, backup, logs, logs-complete]

    def status(self):
        # função que retornar um dicionário dos status do bot
        
        url = f'https://api.squarecloud.app/v1/public/status/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
            
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
            
        return response_json['response']
    
    def status_format(self):
        
        status_dic = self.status()
        
        return f'Status: {status_dic["status"]}\nCpu: {status_dic["cpu"]}\nMemória: {status_dic["ram"]}\nSSD: {status_dic["storage"]}\nNetwork: {status_dic["network"]}\nRequests: {status_dic["requests"]}/200'
    
    
    def backup(self):
        # função que retornar um link pro backup
        
        url = f'https://api.squarecloud.app/v1/public/backup/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
            
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
            
        return response_json['response']['downloadURL']
    
    
    def logs(self):
        # função que retornar todos os ultimos 5 logs do bot
        
        url = f'https://api.squarecloud.app/v1/public/logs/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
            
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
            
        return response_json["response"]["logs"]
        
        
    def log_complete(self):
        # função que retornar um link para as logs completa
        
            url = f'https://api.squarecloud.app/v1/public/logs-complete/{self.id_app}'
            headers = {"Authorization": f"{self.key_api}"}
            response = requests.get(url, headers=headers)
            response_json = json.loads(response.text)
            
            if response_json['status'] == 'error':
                t_erro = square_erro.error(error=response_json['code'])
                
                return t_erro.tratar_erro()
            
            return response_json["response"]["logs"]

# Requests Post --> [start, stop, restart]

    def start(self):
        # função que inicia seu bot
        
        url = f'https://api.squarecloud.app/v1/public/start/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.post(url, headers=headers)
        response_json = json.loads(response.text)
            
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
        
        if self.status()['status'] == 'running':
            return Fore.YELLOW + 'your bot is already running'
            
        return Fore.GREEN + 'Your bot has been started.'

        
    def stop(self):
        # função que para seu bot
        
        url = f'https://api.squarecloud.app/v1/public/stop/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.post(url, headers=headers)
        response_json = json.loads(response.text)
        
        if self.status()['status'] == 'exited':
            return Fore.YELLOW + 'your bot is already stopped'
        
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
        
        return Fore.GREEN + 'Your bot has been stopted.'
        
    def restart(self):
        # função que reiniciar seu bot
        
        url = f'https://api.squarecloud.app/v1/public/restart/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.post(url, headers=headers)
        response_json = json.loads(response.text)
            
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
            
        return Fore.GREEN + 'your bot has restarted'
