from flask import Flask, jsonify, request
from flask_cors import CORS
from vlc import vlc_play, vlc_text

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    print("home")
    return jsonify({"success": True})

@app.route("/play/<path:url>")
def play(url):
    print("play", url)
    vlc_play(url)
    return jsonify({"success": True})

@app.route("/text/<message>")
def text(message):
    print("text", message)
    color = request.args.get("color", "0xFFFFF")
    position = request.args.get("position", "0")
    duration = request.args.get("duration", "10")
    vlc_text(message, color, position, duration)
    return jsonify({"success": True})


