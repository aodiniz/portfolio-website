from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Portfolio</p>"

if __name__ == "__main__":
    app.run(debug=True)
