from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "It's a me! Khalid!"

if __name__ == "__main__":
    app.run()
