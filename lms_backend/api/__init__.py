import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import logging
from sys import stdout

app = Flask(__name__)
app.config.from_object("api.config.Config")
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello!"


# Define logger
logger = logging.getLogger("mylogger")

logger.setLevel(logging.DEBUG)  # set logger level
logFormatter = logging.Formatter(
    "%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s"
)
consoleHandler = logging.StreamHandler(stdout)  # set streamhandler to stdout
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
