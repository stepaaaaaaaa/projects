from flask import (Flask , jsonify)
import requests
from services import Connection

url = 'https://raw.githubusercontent.com/openfootball/football.json/master/2020/jp.1.json'
r = requests.get(url)
app: Flask = Flask(__name__)
conn: Connection = Connection()
conn.create_tables()
conn.data(r.json()['matches'])
conn.match_info()
@app.route('/score/<score>')
def score(score):
    return jsonify(conn.info_score(score=score))



@app.route("/")
def main():
    return """тут ничего нет <br><br><br> а хотя пусть тут будут ссылки <br> <a href='/matches'>Матчи</a> <br> 
        <a href='/teams'>Команды</a> <br> Введите эндпоинт /score/1-2 или 2-2 да все что угодно"""

@app.route('/matches')
def matches():
    return jsonify(conn.match_info())

@app.route('/teams')
def teams():
    return jsonify(conn.teams())

if __name__ == "__main__":
    app.run(debug=True, port=2300)
