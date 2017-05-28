from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    """ Routes to index/homepage. """
    return render_template('index.html')


@app.route("/about")
def about():
    """ Routes to an about me page. """
    pass


@app.route("/myfood")
def myfood():
    """ Routes to the page with my Instagram food pictures. """
    pass


@app.route("/resume")
def resume():
    """ Routes to the page with my resume. """
    pass


@app.route("/mynotes")
def mynotes():
    """ Routes to the page with my notes. """
    pass


if __name__ == "__main__":
    app.run()
