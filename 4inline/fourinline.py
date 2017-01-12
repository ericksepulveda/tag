# define simple flask app
from flask import Flask, render_template, send_from_directory, request
from fourinlineclass import FourInLine
app = Flask(__name__)

fil = FourInLine()

def show():
	return render_template('index.html', board=fil.getBoard(), turn=fil.getTurn(), state=fil.getState())

@app.route('/')
def home():
	return show()

@app.route('/restart')
def restart():
  fil.restart()
  return show()

@app.route('/move', methods=["POST"])
def move():
  r = fil.dropChip(int(request.form['col']))
  fil.check4Horizontal(r[0],r[1])
  return show()

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

if __name__ == "__main__":
    app.run()
