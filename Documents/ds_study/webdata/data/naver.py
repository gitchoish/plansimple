import requests
import pandas as pd
import openpyxl
# from urllib.request
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# soup = BeautifulSoup(requests.get('url').text, 'lxml')
print(soup.prettify())

exchangeList = soup.select('#exchangeList > li')

exchange_datas = []
base_URL = "https://finance.naver.com"

for item in exchangeList:
    data = {
        "title":item.select_one(".h_lst").text,
        "exchange":item.select_one(".value").text,
        "change":item.select_one(".change").text,
        # "updown":item.select_one(".head_info > .blind").text
        'link': base_URL + item.select_one('a').get('href')
    }
    exchange_datas.append(data)
    print(data)
df = pd.DataFrame(exchange_datas)
df.to_excel('./naverfinance2.xlsx')
