# !pip install db-sqlite3

import pandas as pd
import xml.etree.ElementTree as ET
import requests
from urllib.request import urlopen

url = "http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml "
header = { 'Accept': 'application/xml' }
request = requests.get(url, headers=header)
tree =  ET.ElementTree(ET.fromstring(request.content))
root = tree.getroot()

aux = ['SBCF', 'SBRJ', 'SBSP', 'SBVT']
auxEstacao = []
auxAtualizacao = []
auxTemperatura = []
auxUmidade = []

dicionario = {}
for c in range(0,26):
  if root[c][0].text in aux:
    auxEstacao.append(root[c][0].text)      # Estacao
    auxAtualizacao.append(root[c][1].text)  # Atualização
    auxTemperatura.append(root[c][3].text)  # Temperatura
    auxUmidade.append(root[c][6].text)       # Umidade

dicionario['Estação'] = auxEstacao
dicionario['Atualização'] = auxAtualizacao
dicionario['Temperatura'] = auxTemperatura
dicionario['Umidade'] = auxUmidade


tabela = pd.DataFrame(dicionario)
tabela
