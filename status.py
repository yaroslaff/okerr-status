from flask import Flask, render_template
import os
import requests
import json
from urllib.parse import urljoin
from flaskext.markdown import Markdown

from config import textid, name, url


app = Flask(__name__)
Markdown(app)

@app.route('/')
def status():


    if url is None:
        url = '/'.join(['https://cp.okerr.com/jstatus', textid, name])

    r = requests.get(url)
    data = json.loads(r.text)
    return render_template('status.html', **data)

