import requests
from bs4 import BeautifulSoup as bs
import sqlite3
link = requests.get('https://www.pravda.com.ua/news/').content
soup = bs(link, 'lxml').find_all('div', {'class': 'article_header'})

con = sqlite3.connect('../hack_on.db')
cur = con.cursor()

for item in soup:
    url = item.find('a').get('href')
    if url[:5] == '/news':
        url = 'https://www.pravda.com.ua/' + url

    title = item.find('a').text
    id_news = url.split('/')[-2]
    count = cur.execute(f'Select id from news_table where hash = "{id_news}"').fetchall()
    if len(count) == 0:
        cur.execute('Insert into news_table (title, hash, link) values (?, ?, ?)', (title, id_news, url,))
        con.commit()
        print(title + '\nID:' + id_news + '\nlink: ' + url)
