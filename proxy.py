from flask import Flask, request, redirect
import requests

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

@app.route("/<type>/<site>/<path:subpath>")
def test(site, type, subpath):
    url = request.url.replace(f"{site}/{type}/", "").replace(app.config['SERVER_NAME'], site)
    match type:
        case "redirect": return redirect(url)
        case "json": return requests.get(url).json()

app.run(host='0.0.0.0', port=8080)
