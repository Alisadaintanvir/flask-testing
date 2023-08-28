from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/Bye")
@make_bold
@make_emphasis
@make_underline
def user_route():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
