import requests
import json

dados = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
dados = dados.json()
print(dados)
cotacao_dollar = dados['USDBRL'] ['high']
print(cotacao_dollar)

