from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return "http://127.0.0.1:8080/index/название"  # с заботой о вас)))


@app.route('/index/<title>')
def index(title):
    param = {"title": title}
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
