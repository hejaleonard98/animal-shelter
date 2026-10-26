import random
import json

def load_animals(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        animals = json.load(file)
    return animals


def save_animals(file_path, animals):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(animals, file, indent=4)


def show_animals(animals):
    animal_adjectives = [
    "playful", "curious", "friendly", "affectionate", "loyal", "gentle", "shy", "bold",
    "brave", "clever", "smart", "mischievous", "independent", "social", "calm", "energetic",
    "lazy", "sassy", "stubborn", "sweet", "cute", "adorable", "fluffy", "furry", "sleek",
    "tiny", "chubby", "scruffy", "handsome", "pretty", "majestic", "spotted", "striped",
    "cuddly", "sleepy", "hungry", "grumpy", "happy", "excited", "bouncy", "clumsy", "silly",
    "goofy", "cheeky", "alert", "relaxed", "snuggly", "noisy", "quiet", "precious",
    "charming", "lovable", "huggable", "fuzzy", "wiggly", "zoomy", "derpy", "feisty", "spunky",
]
    for animal in animals:
        adjective = random.choice(animal_adjectives)
        print(f"{animal["name"]}, a {animal["age"]} year(s) old {adjective} {animal["type"]}. ID: {animal["id"]}")


def get_available_animals(animals):
    return [animal for animal in animals if animal["available"]]


def find_animal_by_id(animals, animal_id):
    return next((animal for animal in animals if animal["id"] == animal_id), None)


def update_animal_status(animals, adoption):
    animal = find_animal_by_id(animals, adoption["animal_id"])
    if animal:
        animal["available"] = False

