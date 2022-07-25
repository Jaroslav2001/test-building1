from os import system, name
import requests
from bs4 import BeautifulSoup

url = 'https://inlnk.ru/jElywR'
host = 'https://ru.wikipedia.org'
mass: dict[str, int] = {}

rb = True
while rb:
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    contents = soup.find_all(id='mw-pages')
    url = host + soup.find_all(title='Категория:Животные по алфавиту')[1].get('href')

    contents = BeautifulSoup(
        str(contents[0]), 'html.parser'
    ).find_all(class_='mw-category-group')
    for content in contents:
        abc = BeautifulSoup(str(content), 'html.parser')
        if not(abc.find('h3').text in mass):
            if abc.find('h3').text == 'A':
                rb = False
                continue
            mass[abc.find('h3').text] = 0
        mass[abc.find('h3').text] += len(abc.find_all('li'))

    system('cls' if name == 'nt' else 'clear')
    for i, j in mass.items():
        print(f'{i}: {j}')

# urls = []
#
# for link in soup.find_all(class_='external text'):
#     if re.match(r'[А-Я]', link.text):
#         urls.append(link.get('href'))
#
# urls = urls[1:]
#
#
# result = grequests.map(
#     tuple(map(grequests.get, urls))
# )


if __name__ == '__main__':
    for i, j in mass.items():
        print(f'{i}: {j}')
