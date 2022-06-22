from flask import Flask, render_template,url_for
import pyqrcode
from pyqrcode import QRCode
import os
app = Flask(__name__)
picFolder = os.path.join("static","pics")
app.config['uploadFolder'] = picFolder
@app.route("/")
def home():
    image = os.path.join(app.config['uploadFolder'],'myqr.png')
    qr()
    return render_template("./index.html",image1= image)

def qr():
    s = "hello vai"
    url = pyqrcode.create(s)
    url.png('myqr.png')
if __name__ == '__main__':
    app.run(debug=True)

