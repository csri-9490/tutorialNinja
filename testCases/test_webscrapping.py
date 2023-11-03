import pandas
import requests
from bs4 import  BeautifulSoup


def test_webscrap():

       response=requests.get("https://tutorialsninja.com/demo/index.php?route=product/category&path=24")
       soup=BeautifulSoup(response.content,'html.parser')
       print('content',soup)
       print('statuscode is',response.status_code)




