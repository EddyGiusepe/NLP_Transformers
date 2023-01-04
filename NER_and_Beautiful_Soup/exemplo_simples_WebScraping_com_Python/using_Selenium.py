'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo: https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-2/?ref=morioh.com&utm_source=morioh.com
'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

 
option = webdriver.ChromeOptions()
# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome('/home/eddygiusepe/Imagens/Eddy_codigos/NLP_Transformers/NER_and_Beautiful_Soup/exemplo_simples_WebScraping_com_Python/chromedriver_linux64/chromedriver', options=option)
 
page = driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup
 
totalScrapedInfo = [] # In this list we will save all the information we scrape
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    driver.get('https://www.imdb.com/' + anchor['href']) # Access the movie’s page
    infolist = driver.find_element(By.CSS_SELECTOR, '.ipc-inline-list')[0]
    #infolist = driver.find_element(By.CSS_SELECTOR, '.ipc-inline-list')[0] # Find the first element with class ‘ipc-inline-list’
    informations = infolist.find_element("[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
    scrapedInfo = {
        "title": anchor.text,
        "year": informations[0].text,
        "duration": informations[2].text,
    } # Save all the scraped information in a dictionary
    totalScrapedInfo.append(scrapedInfo) # Append the dictionary to the totalScrapedInformation list
    
print(totalScrapedInfo) # Display the list with all the information we scraped
