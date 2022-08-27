from bs4 import BeautifulSoup
import requests

msftUrl = 'https://docs.microsoft.com/en-us/'
msftDocs = requests.get(msftUrl).text
soup = BeautifulSoup(msftDocs, 'lxml')

file = open("data.md", "w")

productDirectory_Section = soup.find(
    'ul', class_="has-three-text-columns").find_all('a', href=True)

productDirectory_Scraped = [(product.text.strip(
), "https://docs.microsoft.com" + product['href']) for product in productDirectory_Section]

file.write("# Product Directories\n\n")
productTemplate = "> {0:30} {1}\n"
for product in productDirectory_Scraped:
    file.write(productTemplate.format(product[0], product[1]))

file.close()
