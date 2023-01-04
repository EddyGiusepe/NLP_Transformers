'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo: https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-2/?ref=morioh.com&utm_source=morioh.com
'''
from bs4 import BeautifulSoup
from selenium import webdriver
 
option = webdriver.ChromeOptions()

# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')

# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome('/home/eddygiusepe/Imagens/Eddy_codigos/NLP_Transformers/NER_and_Beautiful_Soup/exemplo_simples_WebScraping_com_Python/chromedriver_linux64/chromedriver', options=option)
 
driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup. Notice driver.page_source instead of page.content
 
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    print(anchor.text) # Display the innerText of each anchor
