import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("api.config.Config")
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
