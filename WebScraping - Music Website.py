from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def clean(text):
  return text.replace('\r', '').replace('\n', '').strip()

headers = {'Accept-Language': 'en-US,en;q=0.9', 'Accept': 'text/html'}
url = 'https://www.sheetmusicplus.com/en/explore?q=vk&lang=default'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles=[]
links=[]
instruments=[]
cover=[]
price=[]

rows = soup.find_all(class_='product-tile')

for row in rows:
  titles.append(clean(row.find(class_='link').get_text()))
  links.append(row.attrs.get('href'))
  instruments.append(clean(row.find(class_='category').get_text()))
  cover.append(clean(row.find(class_='tile-image').attrs.get('src')))
  price.append(clean(row.find(class_='value').get_text()))

print(titles)
print(links)
print(instruments)
print(cover)
print(price)

df = pd.DataFrame(
    {'title': titles,
     'link': links,
     'instruments': instruments,
     'cover': cover,
     'price': price}
    )

print (df.head())

df.to_csv('musiclist.csv', index=False)