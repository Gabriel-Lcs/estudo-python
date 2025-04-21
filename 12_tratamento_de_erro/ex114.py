#Crie um código em python que teste se o site Www.pudim.com.br está acessível pelo computador usado.
import urllib.request

url = 'https://www.pudim.com.br'
try:
    site = urllib.request.urlopen(url)
except:   
    print('Não foi possível acessar o site Www.pudim.com.br')
else:
    print('Consegui acessar o site Www.pudim.com.br')
