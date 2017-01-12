# define simple flask app
from flask import Flask,render_template, request
from fourinlineclass import FourInLine
app = Flask(__name__)

fil = FourInLine()

def show():
	return render_template('index.html')


@app.route('/')
def home():
	return show()

@app.route('/move', methods=["POST"])
def move(): pass

if __name__ == "__main__":
    app.run()
