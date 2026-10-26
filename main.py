from shelter.animals import load_animals,save_animals,show_animals,get_available_animals,find_animal_by_id,update_animal_status
from shelter.adoptions import load_adoptions,save_adoptions,create_adoption,add_adoption,show_adoptions
import os

def show_menu() -> None:
    print("")
    print("=== ANIMAL SHELTER ===")
    print("Adopt today to save an animal")
    print("")
    print("1. Show available animals")
    print("2. Adopt an animal")
    print("3. Show adoptions")
    print("4. Exit")
    print("")



def main() -> None:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    ANIMALS_FILE = os.environ.get("ANIMALS_FILE", os.path.join(DATA_DIR, "animals.json"))
    ADOPTIONS_FILE = os.environ.get("ADOPTIONS_FILE", os.path.join(DATA_DIR, "adoptions.json"))
    animals: list[dict] = load_animals(ANIMALS_FILE)
    adoptions: list[dict] = load_adoptions(ADOPTIONS_FILE)

    while True:
        show_menu()
        choice: str = input("Choose: ").strip()
        match choice:
            case "1": show_animals(get_available_animals(animals))
            case "2":
                try:
                    animal_id: int = int(input("ID of animal to adopt: ").strip())
                except ValueError:
                    print("Please enter a number.")
                    continue
                animal: dict | None = find_animal_by_id(get_available_animals(animals), animal_id)
                if animal is None:
                    print("No available animal with that ID.")
                    continue
                adopter_name: str = input("What is your name? ").strip()
                add_adoption(animals, adoptions, create_adoption(animal, adopter_name))
            case "3": show_adoptions(adoptions)
            case "4": 
                save_animals(ANIMALS_FILE, animals)
                save_adoptions(ADOPTIONS_FILE, adoptions)
                break
            case _: print("Please choose a valid input!")


if __name__ == "__main__":
    main()
