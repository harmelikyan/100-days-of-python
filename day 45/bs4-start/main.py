from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, 'html.parser')
find_title = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []

for title in find_title:
    title_text = title.getText()
    article_texts.append(title_text)
    title_link = title.get('href')
    article_links.append(title_link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_number)

# print(article_texts)
# print(article_links)
# print(article_upvotes)
