from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello from Flask</h2>"


"""
Because we had the "if" statement in our application file, this will be true if we run this module as a standalone program. As a result, it can function as a module imported by another program or as a standalone program, but it will only execute the code in the if statement if run as a program.
"""
if __name__ == "__main__":
    app.run(debug=True)
