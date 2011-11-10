import os, urllib
from flask import Flask, request, redirect
 
app = Flask(__name__)
    
@app.route('/')
def default():
    return redirect("https://github.com/nixmc/nm-redirector")
    
@app.route('/<path:encoded_url>/')
@app.route('/<path:encoded_url>/<username>/')
def redirector(encoded_url="", username=""):
    useragent = request.headers['User-Agent']
    if useragent in ("bitly","bitlybot","bit.ly"):
        return "Hello bitly"
    else:
        url = urllib.unquote_plus(encoded_url)
        return redirect(url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)