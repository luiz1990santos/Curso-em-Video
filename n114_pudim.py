import requests
try:
    url = 'http://pudim.com.br'
    r = requests.get(url)
except requests.exceptions.ConnectionError:
    print('Site não acessado.')
else:
    print('Site acessado com sucesso.')
