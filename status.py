from flask import Flask, render_template
import os
import requests
import json
from urllib.parse import urljoin
from flaskext.markdown import Markdown

import config

app = Flask(__name__)
Markdown(app)

@app.route('/')
def status():

    name = config.name or ''

    url = config.url or '/'.join(['https://cp.okerr.com/jstatus', config.textid, name])

    r = requests.get(url)
    data = json.loads(r.text)
    return render_template('status.html', **data)
