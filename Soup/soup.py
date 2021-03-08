from bs4 import BeautifulSoup
import lxml
import requests

page = requests.get('http://127.0.0.1:8000/').text

soup = BeautifulSoup(page, 'lxml')

article = soup.find('div', class_='main-text')
inner = soup.find_all('div', class_='main-text')
heading = article('h1')
paragraph = article('p')
links = article('a')

dic = {
    'title': heading,
    'message': paragraph,
    'link': links,
}

#print(article)
print(dic)