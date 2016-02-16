from flask import Flask, render_template, abort
import os

app = Flask(__name__)
app.debug = False


@app.route('/')
def index():
    return page("index")


@app.route('/<page>.html')
def page(page):
    if os.path.exists("templates/" + page + ".html"):
        return render_template(page + ".html")
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1')
