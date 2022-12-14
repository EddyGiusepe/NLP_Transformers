'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# named entity recognition with a web api
import requests
import json
from config import apikey
 
text = "Is YOUR future worth fighting for? We think so. But your support of The Real News is critical to telling the stories of \
    the movements leading those struggles. To help ensure our independence, we must raise $150,000 by MIDNIGHT 12/31. "
headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
body = {
    "text": text
}
url = "https://app.thetextapi.com/text/ner"
 
response = requests.post(url, headers=headers, json=body)
ner = json.loads(response.text)["ner"]
print(ner)
