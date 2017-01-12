# define simple flask app
from flask import Flask,render_template, request
from toqueclass import Toque
app = Flask(__name__)

toque = Toque()

def show(hint):
	return render_template('index.html', hint=hint)

@app.route('/')
def hello_world():
	return show("????")

@app.route('/guess', methods=["POST"])
def guess():
	hint = toque.guess(request.form['guess'])
	return show(hint)

if __name__ == "__main__":
    app.run()
