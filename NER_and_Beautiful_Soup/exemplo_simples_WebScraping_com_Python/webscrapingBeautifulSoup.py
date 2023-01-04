import requests
from bs4 import BeautifulSoup

# Obtendo o HTML da página por meio de solicitação 
page = requests.get('https://www.imdb.com/chart/top/')

# Analisando conteúdo usando beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')

# Selecionando todas as âncoras com títulos 
links = soup.select("table tbody tr td.titleColumn a") 

# Mantenha apenas as 10 primeiras âncoras
first10 = links[:10]
for anchor in first10:
    print(anchor.text) # Exibir o texto interno (innerText) de cada âncora
