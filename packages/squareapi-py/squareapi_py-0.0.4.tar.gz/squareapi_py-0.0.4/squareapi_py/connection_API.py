# squarecloud unofficial API module

#=================================== Imports ======================================#

import requests
import json

from . import square_erro
#===================================================================================#

"""
    modulo que contem as funções que faz todas as requisições a API
    ================================================================
    * R_GET --> faz requisições com o metado GET a api
    * R_POST --> faz requisições com o metado POST a api
"""


class square_connection():
    def __init__(self, url, key_api):
        self.url = url
        self.key_api = key_api
           
    def R_GET(self):
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.get(self.url, headers=headers)
        response_json = json.loads(response.text)
        
        if response_json['status'] == 'error':
            Error_Handling = square_erro.error(error=response_json['code'])
                
            return Error_Handling.tratar_erro()
        
        return response_json
    
    def R_POST(self):
        headers = {"Authorization": f"{self.key_api}"}
        response = requests.post(self.url, headers=headers)
        response_json = json.loads(response.text)
        
        if response_json['status'] == 'error':
            Error_Handling = square_erro.error(error=response_json['code'])
                
            return Error_Handling.tratar_erro()
        
        return response_json['status']