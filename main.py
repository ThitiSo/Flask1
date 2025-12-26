from flask import Flask
from flask import render_template
app = Flask(__name__)

news_items = {
    1: {'id': 1, 
        'title': 'COVID-19 update', 
        'body': 'This is a news on COVID-19'},
    2: {'id': 2, 
        'title': 'Facemasks found', 
        'body': 'Recent news on facemask production'},
    3: {'id': 3,
        'title':'Python 4', 
        'body':'Python 4 will be out soon.... this is FAKE'},
}
@app.route("/")
def hello_world():
    return "<p>Hello, NIG!</p>"

@app.route('/hello/')
def hello_world1():
    return '<h1>Hi my name is Thiti<h2>'

@app.route('/index/')
def index():
    # ...
    return render_template('index.html', 
                           news_items=news_items.values())


@app.route('/news/<id>/')
def show_news_item(id):
    news_item = news_items[int(id)]
    return render_template('news_item.html',
                           id=news_item['id'],
                           title=news_item['title'],
                           body=news_item['body'])