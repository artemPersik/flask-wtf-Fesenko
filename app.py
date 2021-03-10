from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
def start():
    def index(title):
    param = {"title": title}
    return render_template('index.html', **param)


@app.route('/index/<title>')
def index(title):
    param = {"title": title}
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
