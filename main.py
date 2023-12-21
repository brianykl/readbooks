import requests
import argparse
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

def extract_info(url):
    response = requests.get(url, HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title_element = soup.find('td', {'itemprop': 'headline'})
    title = title_element.text.strip() if title_element else "Title not found"

    author_element = soup.find('a', {'itemprop': 'creator'})
    author = author_element.text.strip() if author_element else "Author not found"

    genre_element = soup.find('a', {'href': "ebooks/subject/2594"})
    genre = genre_element.text.strip() if genre_element else "Genre not found"

    downloads_element = soup.find('td', {'itemprop': 'interactionCOunt'})
    downloads = downloads_element.text.strip if downloads_element else "Downloads not found"

    book_info = {
        "title": title,
        "author": author,
        "genre": genre,
        "downloads": downloads
    }

    return book_info

#response = requests.get('https://www.gutenberg.org/ebooks/600', HEADERS)
#soup = BeautifulSoup(response.content, 'html.parser')
#downloads_element = soup.find('td', {'itemprop': 'interactionCount'})
#downloads = downloads_element.text.strip() if downloads_element else "Downloads not found"
#print(downloads)