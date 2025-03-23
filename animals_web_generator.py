import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animal_info(animals_data):
    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "diet" in animal:
            print(f"Diet: {animal['diet']}")
        if "locations" in animal and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")
        if "type" in animal:
            print(f"Type: {animal['type']}")
        print()  # Print a newline for readability

def main():
    animals_data = load_data('animals_data.json')
    print_animal_info(animals_data)

if __name__ == "__main__":
    main()
