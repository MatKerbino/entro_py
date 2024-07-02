import requests
from bs4 import BeautifulSoup

url = 'https://www.freecodecamp.org/news/20-beginner-python-projects/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
names = soup.find_all('li')

print(names)