from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test_route():
	return render_template('testroute.html')

if __name__ == "__main__":
    app.run()