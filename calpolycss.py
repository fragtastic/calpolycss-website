from flask import Flask, render_template

app = Flask(__name__)
app.debug = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<page>.html')
def page(page):
    return render_template(page + ".html")


if __name__ == '__main__':
    app.run(host='127.0.0.1')
