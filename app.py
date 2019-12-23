# app.py - a minimal flask api using flask_restful
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()