import os
from flask import Flask, request, redirect
 
app = Flask(__name__)
    
@app.route('/')
@app.route('/<username>')
def redirector(username="nothing"):
    return redirect("http://www.google.com/?q=" + username)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)