from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/proxy')
def get_stuff():
    return requests.get(request.args.get('url')).content

app.run()