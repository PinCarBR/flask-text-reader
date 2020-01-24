import os
from flask import Flask, render_template

app = Flask(__name__)

# A random secret used by Flask to encrypt session data cookies
app.secret_key = os.environ['FLASK_SECRET_KEY']
fileDir = os.environ['FILE_DIR'] 
fileName = os.environ['FILE_NAME']
filePath = fileDir + fileName 

@app.route('/')
def content():
    text = open(filePath,  'r')
    content = text.read()
    text.close()
    return render_template('content.html', text=content)


if __name__ == '__main__':
    app.run()
