from flask import Flask, request
import json
import logging

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return "<h1>You're not supposed to see this, silly!</h1>"
    elif request.method == "POST":
        message = request.get_json()
        app.logger.info("[{}] {}: {}".format(message["sender_id"], message["name"], message["text"]))
        return ""