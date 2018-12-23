from flask import Flask, request
import pprint # debugging json requests
import json

app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=4)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return "<h1>You're not supposed to see this, silly!</h1>"
    elif request.method == "POST":
        message = request.get_json()
        print("[{}] {}: {}".format(message["sender_id"], message["name"], message["text"]))
        return ""