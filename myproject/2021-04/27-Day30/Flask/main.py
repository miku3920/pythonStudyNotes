# main.py
from flask import Flask, request
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route("/post_submit", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'Hello ' + request.form.get('username')
    return render_template('post_submit.html')


@app.route("/")
def root():
    return render_template('post_submit.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
