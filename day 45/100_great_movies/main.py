from bs4 import BeautifulSoup
import requests


response = requests.get('https://web.archive.org/web/20200518073855'
                        '/https://www.empireonline.com/movies/features/best-movies-2/')

movies_web_page = response.text


soup = BeautifulSoup(movies_web_page, 'html.parser')
find_title = soup.find_all(name='h3', class_='title')

list_titles = [title.getText() for title in reversed(find_title)]
with open('100_movies.txt', 'w') as f:
    for title in list_titles:
        f.write("%s\n" % title)
