from flask import Flask
from datetime import datetime
from random import randint
import time
app = Flask(__name__)
@app.route("/")
def t():
    color = ''
    name = 'gal'
    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    value = randint(0, 5)
    if value == 1:
        color = 'blue'
    elif value == 2:
        color = 'yellow'
    elif value == 3:
        color = 'green'
    elif value == 4:
        color = 'grey'
    elif value == 5:
        color = 'purple'
    return '''
       <html>
    <head>
        <title>HTML in 10 Simple Steps or Less</title>
    </head>
    <body style="background-color:{};">>
    <h2>{}, Current Time is: {}</h2>
    </body>
    </html>
        '''.format(color,name,current)
@app.route("/gal")
def g():
    return'''<html><head><b>HAIDEEEE!!!!!</b></head></html>'''
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
