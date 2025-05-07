from flask import Flask, request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from requests import get

app = Flask(__name__)

@app.route('/proxy')
def get_stuff():
    soup = BeautifulSoup(get(request.args.get('url')).content, 'html.parser')
    for a in soup.find_all('a'):
        href = a['href']
        if href.startswith('/'):
            href = urlparse(request.args.get('url')).netloc + href
        if not href.startswith('http'):
            href = 'https://' + href
        a['href'] = f"{request.base_url}?url={href}"
    return str(soup)

app.run()