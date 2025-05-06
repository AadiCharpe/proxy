from flask import Flask, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/proxy')
def get_stuff():
    soup = BeautifulSoup(requests.get(request.args.get('url')).content, 'html.parser')
    for a in soup.find_all('a'):
        a['href'] = f"{request.base_url}?url={a['href']}"
    return str(soup)

app.run()