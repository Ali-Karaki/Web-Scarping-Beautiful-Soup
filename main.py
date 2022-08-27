from bs4 import BeautifulSoup
import requests

# Use requests to access the web page, and create BeautifulSoup instance
msftUrl = 'https://docs.microsoft.com/en-us/'
msftDocs = requests.get(msftUrl).text
soup = BeautifulSoup(msftDocs, 'lxml')

# Write results to data.md
file = open("data.md", "w")

# Locate section
productDirectory_Section = soup.find(
    'ul', class_="has-three-text-columns").find_all('a', href=True)

# Get products displayed (name + link)
productDirectory_Scraped = [(product.text.strip(
), "https://docs.microsoft.com" + product['href']) for product in productDirectory_Section]

file.write("# Product Directories\n\n")

# Add products to file
productTemplate = "> {0:30} {1}\n"
for product in productDirectory_Scraped:
    file.write(productTemplate.format(product[0], product[1]))

file.close()
