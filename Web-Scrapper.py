import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
names=soup.find_all("a",class_="title")
prices=soup.find_all("h4",class_="price float-end card-title pull-right")
desc=soup.find_all("p",class_="description card-text")
reviews=soup.find_all("p",class_="review-count float-end")
p_elements = soup.find_all('p', attrs={'data-rating': True})
ratings_list = [p['data-rating'] for p in p_elements]

names_list=[]
prices_list=[]
desc_list=[]
reviews_list=[]
for i in names:
    names_list.append((i.text))
for i in prices:
    prices_list.append((i.text))

for i in desc:
    desc_list.append((i.text))

for i in reviews:
    reviews_list.append((i.text))

df=pd.DataFrame({"Product Name":names_list,"Price":prices_list,"Description":desc_list,"Rating":ratings_list,"Reviews":reviews_list})
print(df)
df.to_csv("Test.csv")

