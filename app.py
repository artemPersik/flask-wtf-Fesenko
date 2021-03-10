from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return """<a href="http://127.0.0.1:8080/auto_answer/анкета/Огурцов/Валера/высшее/Инженер/муж/хочу/да">в строке</a> <br>
                <a href="http://127.0.0.1:8080/answer">уже готово</a> <br>"""  # с заботой о вас 2.0


@app.route('/auto_answer/<title>/<surname>/<name>/<education>/<profession>/<sex>/<motivation>/<ready>')
def index(title, surname, name, education, profession, sex, motivation, ready):
    params = {"title": title,
              "style": url_for('static', filename='css/style.css'),
              "surname": surname,
              "name": name,
              "education": education,
              "profession": profession,
              "sex": sex,
              "motivation": motivation,
              "ready": ready}
    return render_template('auto_answer.html', **params)


@app.route("/answer")
def answer():
    params = {"title": "ответ",
              "style": url_for('static', filename='css/style.css'),
              "surname": "surname",
              "name": "name",
              "education": "education",
              "profession": "profession",
              "sex": "sex",
              "motivation": "motivation",
              "ready": "ready"}
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
