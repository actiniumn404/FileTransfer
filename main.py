from flask import Flask, render_template, request, jsonify
from pathlib import Path
import logging
import urllib

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True # TODO: Toggle to False
logging.getLogger('werkzeug').setLevel(logging.ERROR)

if not Path("storage/clipboard.txt").is_file():
    with open("storage/clipboard.txt", "w") as file:
        file.write("")


@app.route('/')
def home():  # put application's code here
    with open("storage/clipboard.txt") as f:
        return render_template("home.html", address=request.host, text=f.read())


@app.route('/api/change', methods=["POST"])
def api_change():
    raw = request.json

    if "text" not in raw.keys():
        return jsonify({"error": "Missing required parameter: text"}), 400

    with open("storage/clipboard.txt", "w") as file:
        file.write(raw["text"])

    return jsonify({"success": "Success"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8008)
