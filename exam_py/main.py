from flask import Flask, render_template, request

from names import names, passwords

app = Flask(__name__)

@app.route('/')
def main():
    return """<a href='http://localhost:5000/admin'>Авторизация и посты тут</a>
            <a href='http://localhost:5000/calculator'>Калькулятор в одну строчку тут</a>"""




@app.route('/calculator')
def calc():
    return render_template("calculator.html")






@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == names["name"] and password == passwords["password"]:
            return render_template("posts.html", name = names["name"], name2 = names["name2"], name3 = names["name3"], name4 = names["name4"], name5 = names["name5"])
        else:
            return "Неверный логин или пароль"

    return render_template('admin.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)