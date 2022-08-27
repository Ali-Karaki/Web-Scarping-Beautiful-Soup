from bs4 import BeautifulSoup
import requests


siteUrl = 'https://docs.microsoft.com/en-us/'
azureDocs = requests.get(siteUrl).text
soup = BeautifulSoup(azureDocs, 'lxml')

productDirectory_Section = soup.find('ul', class_="has-three-text-columns").find_all('a')
productDirectory_Scraped = [product.text.strip() for product in productDirectory_Section]
# print(productDirectory_Scraped)

