from flask import Flask, request, render_template
from nba_predict import predict

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name=None):
	return render_template("playground.html", name=name)

if __name__ == "__main__":
	app.run(debug=True)