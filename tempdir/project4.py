from flask import Flask
from flask import request
from flask import render_template


midterm = Flask (__name__, static_url_path='')

@midterm.route('/', methods= ['GET', 'POST'])
def main():
    return render_template("login.html")


@midterm.route('/registration.html', methods = ['GET', 'POST'])
def registration():
    return render_template('registration.html')


if __name__ == "__main__":
    midterm.run(host="0.0.0.0",port=5000)