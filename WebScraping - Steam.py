from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def clean(text):
  return text.replace('\r', '').replace('\n', '').strip()

headers = {'Accept-Language': 'en-US,en;q=0.9', 'Accept': 'text/html'}
url = 'https://store.steampowered.com/search/?filter=topsellers'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles=[]
links=[]
date_released=[]
cover=[]
final_price=[]

rows = soup.find_all(class_='search_result_row')

for row in rows:
  titles.append(clean(row.find('span', class_='title').get_text()))
  links.append(clean(row.attrs.get('href')))
  date_released.append(clean(row.find(class_='search_released').get_text()))
  cover.append(clean(row.find('img').attrs.get('src')))
  final_price.append(clean(row.find(class_='search_price_discount_combined').get_text()))

print(titles)
print(links)
print(date_released)
print(cover)
print(final_price)

df = pd.DataFrame(
    {'game title': titles,
     'link': links,
     'date released': date_released,
     'game cover': cover,
     'price': final_price}
    )

print (df.head())

df.to_csv('steamtopsellers.csv', index=False)