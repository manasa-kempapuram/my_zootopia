import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_info(animals_data):
    """Generates HTML content for the animals list."""
    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        if "diet" in animal:
            output += f'    <strong>Diet:</strong> {animal["diet"]}<br/>\n'
        if "locations" in animal and animal["locations"]:
            output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        if "type" in animal:
            output += f'    <strong>Type:</strong> {animal["type"]}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'
    return output


def create_html(animals_data):
    """Reads template HTML, replaces placeholder, and writes to a new file."""
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    animals_info = generate_animal_info(animals_data)
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as output_file:
        output_file.write(new_html_content)


def main():
    """Main function to load data and generate the HTML file."""
    animals_data = load_data('animals_data.json')
    create_html(animals_data)


if __name__ == "__main__":
    main()
