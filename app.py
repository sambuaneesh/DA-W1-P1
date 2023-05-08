from flask import Flask, jsonify, render_template, request
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


anime_titles = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "Fullmetal Alchemist",
    "Death Note",
]
anime_descriptions = [
    "A story about a young ninja",
    "A story about a pirate crew",
    "A story about fighting titans",
    "A story about alchemy",
    "A story about a notebook that can kill people",
]


@app.route("/generate_title", methods=["POST"])
def generate_title():
    title = random.choice(anime_titles)
    description = random.choice(anime_descriptions)
    return jsonify({"title": title, "description": description})


if __name__ == "__main__":
    app.run(debug=True)
