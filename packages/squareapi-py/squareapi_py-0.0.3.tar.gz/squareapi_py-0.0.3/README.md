# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Squareapi-py 0.0.3

pt-br : biblioteca não oficial da [squarecloud](https://squarecloud.app).
en: [squarecloud](https://squarecloud.app) unofficial library.

**Key_api:**
--------

- para a biblioteca funcionar e necessario ter a chave da api para isso vá no site da [Squarecloud](https://squarecloud.app) e siga o tutorial abaixo: 

> `dashbord -> My account -> API/CLI KEY`

- Com a key_api em mãos agora você está pronto para prosseguir

**Instalando:**
-----------

 primeiramente voce ira digitar o seguinte codigo no terminal do seu projeto

```
$ pip install squareapi-py
```
após a instalação da biblioteca você ira seguir para proxima etapa

**Usando:**
-------
- **Se conectando a api:**
> para se conectar a api você ira importar a lib no seu projeto com `from squarecloud_py import app` logo após, ira passar o id do seu bot junto com a ky_api que você pegou mais cedo.

> Usando a função `Client()` iremos enviar as informações para se conectar.

```py
from squarecloud_py import app

id_app = ''
key_api = ''

bot = app.Client(id_app= id_app, key_api= key_api) #Se conectando a API
```

- **Start/stop/restart:**
> ultilizando as funções [`start() stop() restart()`] você controla o estado do seu bot com poucas linhas de codigos
```py
from squarecloud_py import app

id_app = ''
key_api = ''

bot = app.Client(id_app= id_app, key_api= key_api) #Se conectando a API

bot.start() #ligando o bot
bot.stop() #parando o bot
bot.restart() #reiniciando o bot
```

- **Coletando os logs:**

> usando a função `logs()` o sistema ira fazer um request na API e a função ira retorna as ultimas 5 logs do seu bot

- **Nota:**
> ultilizando `log_complete()` a função ira retorna um link pro site da squarecloud com todas as logs do bot

```py
from squarecloud_py import app

id_app = ''
key_api = ''

bot = app.Client(id_app=id_app, key_api=key_api) #Se conectando a squarecloud

print(bot.logs()) #ou log_complete
```

**Para mais exemplos veja esse [repositorio](https://github.com/4str0x/squareapi-py-exemplos-):**