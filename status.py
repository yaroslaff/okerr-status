from flask import Flask, render_template
import os
import requests
import json
from urllib.parse import urljoin
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

@app.route('/')
def status():
    textid = os.getenv('STATUS_TEXTID')
    name = os.getenv('STATUS_NAME', '')
    url = os.getenv('STATUS_URL')

    if url is None:
        url = '/'.join(['https://cp.okerr.com/jstatus', textid, name])

    r = requests.get(url)
    data = json.loads(r.text)
    return render_template('status.html', **data)

