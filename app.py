from flask import Flask, jsonify, render_template, request, send_file
import random
import json

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Import adjectives
with open("data/adjs.json") as f:
    adjectives = json.load(f)["adjs"]

# Load nouns
with open("data/nouns.json") as f:
    nouns = json.load(f)["nouns"]

# Import verbs
with open("data/verbs.json") as f:
    verbs = json.load(f)["verbs"]

with open("data/settings.json") as f:
    settings = json.load(f)["settings"]


def generate_name():
    title = (
        random.choice(adjectives).title().replace("_", " ")
        + " "
        + random.choice(nouns).title().replace("_", " ")
        + " "
        + random.choice(verbs)["present"].title().replace("_", " ")
        + " "
        + random.choice(settings).title().replace("_", " ")
    )
    return title


# define a function to generate a random anime description
def generate_description():
    description = (
        "In a "
        + random.choice(settings).lower().replace("_", " ")
        + ", a "
        + random.choice(adjectives).lower().replace("_", " ")
        + " "
        + random.choice(nouns).lower().replace("_", " ")
        + " "
        + random.choice(verbs)["present"].lower().replace("_", " ")
        + " "
        + random.choice(settings).lower().replace("_", " ")
        + "."
    )
    return description.capitalize()


@app.route("/")
def serve_html():
    return send_file("index.html")


@app.route("/generate_title", methods=["POST"])
def generate_title():
    title = generate_name()
    description = generate_description()
    return jsonify({"title": title, "description": description})


if __name__ == "__main__":
    app.run(debug=True)
