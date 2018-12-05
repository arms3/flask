from flask import Flask, render_template  # , request, redirect
from fetch_price import fetch, to_html
from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np

app = Flask(__name__)
df = fetch()


def create_figure(feat_name, bins):
    hist, edges = np.histogram(df[feat_name].astype('float'), density=True,
            bins=bins)
    p = figure(title=feat_name, tools='', width=600, height=400)
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
            fill_color="navy")
    p.xaxis.axis_label = feat_name
    p.yaxis.axis_label = 'Count'
    return p


@app.route('/')
def index():
    plot = create_figure('adj_close', 10)
    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template('index.html', script=script, div=div,
        table=to_html(df))


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=33507, debug=True)  # Must remove debug
