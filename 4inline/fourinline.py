# define simple flask app
from flask import Flask, render_template, send_from_directory, request, redirect
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
  return show()

@app.route('/move', methods=["POST"])
def move():
  r = fil.play(int(request.form['col']))
  return redirect('/')
  # return show()

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@app.route('/mp3/<path:path>')
def send_mp3(path):
    return send_from_directory('static/mp3', path)

if __name__ == "__main__":
    app.run()
