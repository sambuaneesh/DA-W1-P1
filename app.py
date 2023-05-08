from flask import Flask, jsonify, render_template, request
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


adjectives = [
    "Magical",
    "Legendary",
    "Epic",
    "Mysterious",
    "Chaotic",
    "Cute",
    "Fierce",
    "Galactic",
    "Enchanted",
]
nouns = [
    "Warrior",
    "Sword",
    "Dragon",
    "Hero",
    "Princess",
    "Samurai",
    "Ninja",
    "Robot",
    "Adventure",
]
verbs = [
    "Fights",
    "Defeats",
    "Saves",
    "Conquers",
    "Discovers",
    "Travels",
    "Explores",
    "Transforms",
    "Escapes",
]
settings = [
    "Fantasy World",
    "Outer Space",
    "Futuristic City",
    "Medieval Kingdom",
    "Underwater Kingdom",
    "Magical Forest",
    "Post-Apocalyptic Wasteland",
    "Alternate Dimension",
]


def generate_name():
    title = (
        random.choice(adjectives)
        + " "
        + random.choice(nouns)
        + " "
        + random.choice(verbs)
        + " "
        + random.choice(settings)
    )
    return title


# define a function to generate a random anime description
def generate_description():
    description = (
        "In a "
        + random.choice(settings)
        + ", a "
        + random.choice(adjectives)
        + " "
        + random.choice(nouns)
        + " "
        + random.choice(verbs)
        + " "
        + random.choice(settings)
        + "."
    )
    return description


@app.route("/generate_title", methods=["POST"])
def generate_title():
    title = generate_name()
    description = generate_description()
    return jsonify({"title": title, "description": description})


if __name__ == "__main__":
    app.run(debug=True)
