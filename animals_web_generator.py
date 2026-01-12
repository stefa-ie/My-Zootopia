import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as fobj:
        return json.load(fobj)


def serialize_animal(animal_obj):
    """Serialize a single animal object to HTML."""
    output = '<li class="cards__item">\n'
    if 'name' in animal_obj:
        output += f"<div class='card__title'>{animal_obj['name']}</div><br/>\n"
    output += "<p class='card__text'>\n"
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
    if 'locations' in animal_obj and animal_obj['locations']:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
    output += '</p>\n'
    output += '</li>\n'
    return output


def serialize_all_animals(animals_data):
    """Serialize all animals to HTML."""
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def generate_html(template_path, animals_html, output_path):
    """Generate HTML file from template and animals HTML."""
    with open(template_path, 'r') as file:
        content = file.read()
    
    updated_content = content.replace('__REPLACE_ANIMALS_INFO__', animals_html)
    
    with open(output_path, 'w') as file:
        file.write(updated_content)


def main():
    """Main function to organize the HTML generation."""
    animals_data = load_data('animals_data.json')
    animals_html = serialize_all_animals(animals_data)
    generate_html('animals_template.html', animals_html, 'animals.html')


if __name__ == "__main__":
    main()
