from flask import Flask, render_template  # , request, redirect
from fetch_price import fetch

app = Flask(__name__)


@app.route('/')
def index():
    tbl = fetch()
    return render_template('index.html', table=tbl)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=33507, debug=True)  # Must remove debug
