def load_adoptions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        adoptions = file
    return adoptions


def save_adoptions(file_path, adoptions):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(adoptions)


def create_adoption(animal, adopter_name):
    return {"animal_id":animal["id"], "animal_name":animal["name"], "adopter": adopter_name}


def add_adoption(adoptions, adoption):
    adoptions.append(adoption)


def show_adoptions(adoptions):
    for number,adoption in enumerate(adoptions, start=1):
        print(f"{number}. {adoption["animal_name"]} adopted by {adoption["adopter"]}")