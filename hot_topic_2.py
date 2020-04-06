

from bs4 import BeautifulSoup as soup
import json
import threading
import randomheaders
from discord_webhook import DiscordWebhook
import requests
import time
from proxies1 import proxie_ip
import datetime


x = (str(datetime.datetime.now())[0:19])

keyword = 'Funko'
filename = 'hottopic.txt'
webhook_url = 'https://discordapp.com/api/webhooks/585416909235683330/dt5q6hCKDsNT4jxY8v0B13Tw0R7p_mimBhpw9q0My1SATuIGEQXSPAbfE9QfMREMJWHC'

def monitor():
    source =  requests.get('https://www.hottopic.com/funko/?srule=sortingNewArrival&sz=60&start=0', headers = randomheaders.LoadHeader()).text
    page_soup = soup(source, "html.parser")
    for items in page_soup.find_all('a', title=True):
        if keyword in items['title']:
            href = items['href']            
            with open(filename, 'r') as rf:
                with open(filename, 'a') as af:
                    read = rf.read()
                    if href not in read:
                        print(href)
                        af.write('\n'+ href)
                        contents = str(x) +'\n'+ href
                        #webhook = DiscordWebhook(url= webhook_url, content= contents )
                        #webhook.execute()
                        print(contents)

                            
                    #else:
                        #print('no new item')
                        

    
    #time.sleep(60)

#while True:
monitor()

