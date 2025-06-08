from flask import Flask, request, redirect
import requests

app = Flask(__name__)

@app.route("/<type>/<site>/<path:subpath>")
def test(site, type, subpath):
    url = request.url.replace(f"{type}/{site}", "")
    url = url.replace(request.url_root, site)
    if not url.startswith("https://"): url = "https://" + url
    match type:
        case "url": return url
        case "redirect": return redirect(url)
        case "json": return requests.get(url).json()

app.run(host='0.0.0.0', port=8080)
