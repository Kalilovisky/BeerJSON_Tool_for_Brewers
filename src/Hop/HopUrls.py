import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
from src.Hop.HopStrain import HopStrain

 
class HopUrls:

    def __init__(self):
        self.hopList = []
        self.url     = 'https://beermaverick.com'
       
    def getHopList(self):
        reqs = requests.get(self.url + "/hops/")
        soup = BeautifulSoup(reqs.text, 'html.parser')
        
        urls = []
        for link in soup.find_all('a'):
            if link.get('href')[0:5] == '/hop/':
                urls.append(link.get('href'))
        
        return urls
    
    def createHopBeerJSON(self, urlList):        
        for i in urlList:
            fullurl = self.url + i
            reqs    = requests.get(fullurl)
            soup    = BeautifulSoup(reqs.content, 'html.parser')
            
            products = soup.find_all('pre')
            frame    = pd.DataFrame(products).__str__()
            partner  = 'data-hop="(.*?)"'
            hopID    = re.search(partner, frame)

            self.__getHopData(hopID.group(1))
        
        self.__save_to_json()
    
    def __getHopData(self, hopID):
        url  = self.url + '/api/js/?hop=' + hopID
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        html_str = soup.find_all('h1').__str__()
        hopName  = re.search('<a.*?>(.*?)</a>', html_str).group(1).strip()
        
        html_str   = soup.find_all('div').__str__() 
        alpha_acid = re.search(r'Alpha Acids:\s*<b>([\d.-]+)%</b>', html_str).group(1).strip() 
        purpose    = re.search(r'Purpose:\s*<b>(\w+)</b>', html_str).group(1).strip() 
        country    = re.search(r'Country:\s*<b>(\w+)</b>', html_str).group(1).strip() 
        profile    = re.search(r'<li><b>Profile:</b>(.*?)</li>', html_str).group(1).strip().replace('&amp;', "") 
        beta_acids = re.search(r'Beta Acids: <b>(.*?)%</b>', html_str).group(1).strip()
        cohumulone = re.search(r'Cohumulone: <b>(.*?)%</b>', html_str).group(1).strip()

        hopStrain = HopStrain(hopName, country, alpha_acid, purpose, beta_acids, profile, cohumulone)
        self.hopList.append(hopStrain)
    
    def __to_json(self, hopList):
        hopStrainList = [hopStrain.to_json() for hopStrain in hopList]
        return {"hop_strains": hopStrainList}
        
    def __save_to_json(self):       
        data = self.__to_json(self.hopList)
        with open("Hop.json", "w") as f:
            json.dump(data, f)