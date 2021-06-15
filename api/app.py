from flask import Flask, jsonify, request
import json
from .html_2txt import scrapeSite

app = Flask(__name__)


@app.route("/")
def home():
    return('Welcome to the Flask ML API Production Demo')


@app.route("/scrape_site")
def classification():
    url = json.loads(request.data)["url"]
    return jsonify(scrapeSite(url))



#if __name__ == '__main__':
#   app.run(host='0.0.0.0')
#use if vpn blocks host 
if __name__ == '__main__':
    app.run(debug=True)