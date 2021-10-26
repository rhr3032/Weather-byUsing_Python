from bs4 import BeautifulSoup
import requests

url = "URL"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

print('Resumo: '+ soup.find(class_='gray -line-height-24 _center').text)
print('Temp Minima: '+ soup.find(id='main-temp-1').string)
print('Temp Maxima: '+ soup.find(id='max-temp-1').string)