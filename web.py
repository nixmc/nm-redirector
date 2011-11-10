import os
from flask import Flask, request, redirect
 
app = Flask(__name__)
    
@app.route('/')
@app.route('/<username>')
def redirector(username="nothing"):
    useragent = request.headers['User-Agent']
    
    if useragent == "bitly" or useragent == "bitlybot" or useragent == "bit.ly":
        return "Hello bitly"
    else:
        return redirect("http://www.google.com/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)