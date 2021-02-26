from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return """<a href="http://127.0.0.1:8080/list_prof/ol">ol</a> <br>
                <a href="http://127.0.0.1:8080/list_prof/ul">ul</a> <br>
                <a href="http://127.0.0.1:8080/list_prof/бомж">бомж</a>"""  # с заботой о вас 2.0


@app.route('/list_prof/<param>')
def index(param):
    if param == "ol" or param == "ul":
        jobs = ["врач", "инженер", "сантехник", "бомж", "пилот", "биолог"]
        return render_template("index.html", jobs=jobs, param=param)
    else:
        return f"""<img src="{url_for('static', filename='img/error.png')}">"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
