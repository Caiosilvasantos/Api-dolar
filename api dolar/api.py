import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

cotacao_dolar = cotacoes['USDBRL']['bid']
#print(cotacao_dolar)

cotacao_euro = cotacoes['EURBRL']['bid']
#print(cotacao_euro)

cotacao_bitcoin = cotacoes['BTCBRL']['bid']
#print(cotacao_bitcoin)

print(cotacoes)
