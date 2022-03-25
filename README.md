# micro-service
Acesso api com python usando FastApi
serviços acessados 
  Spotify API 
  OpenWeatherMaps API

O FastAPI é um framework Python focado no desenvolvimento de API’s, tem como principais características ser moderno, rápido e simples. É um framework relativamente novo, teve a sua primeira versão lançada no dia 15 de Novembro de 2018, mas não se engane, apesar de ser novo ele não é inferior aos outros frameworks que já estão no mercado há mais tempo, como o Django ou o Flask.
Segue link da documentação do fastapi https://fastapi.tiangolo.com/

A linguagem utilizada para desenvolvimento foi a Python, e a IDE foi PyCharm.

Para consultar temperatura pelo nome da cidade, usa o seguinte comando
    http://localhost:8000/city/{city}
    Colocando a cidade São Critovão obtive o seguinte resultado:
    {"Info":"São Cristóvão","Temp":"26.95","url":"https://open.spotify.com/playlist/37i9dQZF1DWVLcZxJO5zyf"}
Para Consuta com coordenadas latitude e longetude, usa o seguinte comando
    http://localhost:8000/Cord/{lat}&{lon}
    Colocando a latitude (-20.3856) e longetude (-43.5035) obtive o seguinte resultado:
    {"Info":"cord-20.3856/-43.5035","Temp":"16.12","url":"https://open.spotify.com/playlist/37i9dQZF1DWVLcZxJO5zyf"}

Objetivo: 

Crie um micro-serviço capaz de aceitar requisições RESTful recebendo como parâmetro o nome da cidade ou as coordenadas longitudinais e retorne uma sugestão de playlist de acordo com a temperatura atual.

Regras:

    Se a temperatura (celcius) estiver acima de 30 graus, sugira faixas para festa
    Caso a temperatura esteja entre 15 e 30 graus, sugira faixas de música pop
    Se estiver um pouco frio (entre 10 e 14 graus), sugira faixas de rock
    Caso contrário, se estiver congelando lá fora, sugere faixas de música clássica
  
 Instalação: 
 
 Para inicializarmos o ambiente virtual, o primeiro passo é estar na pasta criada para o projeto e rodar o seguinte código no terminal Linux:
      python3 -m venv .venv 
      source .venv/bin/activate
 
 Segui com o uvicorn como sendo o servidor ASGI, também utilizado na documentação oficial da linguagem.
      pip install fastapi uvicorn
      
 No terminal, digita o seguinte comando para iniciar o servidor e rodar no seu browser a FastAPI:
      uvicorn main:app --reload
 
 Para acessar o dicionario de dados execute em seu navegador:
      http://127.0.0.1:8000/docs
 
