from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return """<a href="http://127.0.0.1:8080/training/врач">врач</a> <br>
                <a href="http://127.0.0.1:8080/training/инженер">инженер</a> <br>
                <a href="http://127.0.0.1:8080/training/сантехник">сантехник</a> <br>
                <a href="http://127.0.0.1:8080/training/бомж">бомж</a>"""  # с заботой о вас 2.0


@app.route('/training/<prof>')
def index(prof):
    profs = {"врач": url_for('static', filename='img/doctor.png'),
             "инженер": url_for('static', filename='img/ingener.png'),
             "сантехник": url_for('static', filename='img/santeh.png')}
    
    for i in profs:
        if i in prof.lower():
            print(profs[prof])
            return render_template("index.html", schem=profs[prof])
        else:
            return render_template('index.html', schem=url_for('static', filename='img/error.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
