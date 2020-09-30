from flask import Flask, jsonify, request
from flask_cors import CORS
from vlc import vlc_play, vlc_text

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    print("home")
    return jsonify(
        {
            "success": True,
            "example_red_text": request.url_root
            + "text/Hello%20World%20!?duration=5&color=0xFF0000",
            "example_remote_video": request.url_root
            + "play/http://techslides.com/demos/sample-videos/small.mp4",
        }
    )


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
