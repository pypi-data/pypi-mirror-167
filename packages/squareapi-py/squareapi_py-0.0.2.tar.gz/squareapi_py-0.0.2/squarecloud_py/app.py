import requests
import colorama
from colorama import Fore
import json
colorama.init(autoreset=True)

from . import square_erro

class Client():
    def __init__(self, key_api, id_app):
        self.key_api = key_api
        self.id_app = id_app

# Requests GET: --> [status, backup, logs, logs-complete]

    def status(self):
        url = f'https://api.squarecloud.app/v1/public/status/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
            
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
            
        return response_json['response']
    
    def backup(self):
        url = f'https://api.squarecloud.app/v1/public/backup/{self.id_app}'
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
            
        if response_json['status'] == 'error':
            t_erro = square_erro.error(error=response_json['code'])
                
            return t_erro.tratar_erro()
            
        return response_json['response']['downloadURL']
    
    def logs(self):
            url = f'https://api.squarecloud.app/v1/public/logs/{self.id_app}'
            headers = {"Authorization": f"{self.key_api}"}
            response = requests.get(url, headers=headers)
            response_json = json.loads(response.text)
            
            if response_json['status'] == 'error':
                t_erro = square_erro.error(error=response_json['code'])
                
                return t_erro.tratar_erro()
            
            return response_json["response"]["logs"]
        
    def log_complete(self):
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
        try:
            url = f'https://api.squarecloud.app/v1/public/start/{self.id_app}'
            headers = {"Authorization": f"{self.key_api}"}
            
            if self.status()['status'] == 'running':
                return Fore.YELLOW + 'your bot is already running'
            
            else:    
                response = requests.post(url, headers=headers)
            
            response_json = json.loads(response.text)
            
            if response_json['status'] == 'error':
                t_erro = square_erro.error(error=response_json['code'])
                
                return t_erro.tratar_erro()
            
            return Fore.GREEN + 'Your bot has been started.'
        
        except:
            return 'ocorreu um erro patrão'
        
    def stop(self):
        try:
            url = f'https://api.squarecloud.app/v1/public/stop/{self.id_app}'
            headers = {"Authorization": f"{self.key_api}"}
            if self.status()['status'] == 'exited':
                return Fore.YELLOW + 'your bot is already stopped'
            
            else:    
                response = requests.post(url, headers=headers)
            response_json = json.loads(response.text)
            
            if response_json['status'] == 'error':
                t_erro = square_erro.error(error=response_json['code'])
                
                return t_erro.tratar_erro()
            
            return Fore.GREEN + 'your bot has been stopped'
        
        except:
            return 'ocorreu um erro patrão'
        
    def restart(self):
        try:
            url = f'https://api.squarecloud.app/v1/public/restart/{self.id_app}'
            headers = {"Authorization": f"{self.key_api}"}
            response = requests.post(url, headers=headers)
            response_json = json.loads(response.text)
            
            if response_json['status'] == 'error':
                t_erro = square_erro.error(error=response_json['code'])
                
                return t_erro.tratar_erro()
            
            return Fore.GREEN + 'your bot has restarted'
        
        except:
            return 'ocorreu um erro patrão'