import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ""
for animal in animals_data:
    if 'name' in animal:
        output += f"Name: {animal['name']}\n"

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output += f"Diet: {animal['characteristics']['diet']}\n"

    if 'locations' in animal and animal['locations']:
        output += f"Location: {animal['locations'][0]}\n"

    if 'characteristics' in animal and 'type' in animal['characteristics']:
        output += f"Type: {animal['characteristics']['type']}\n\n"

print(output)

with open('animals_template.html', 'r') as file:
    content = file.read()

print(content)

updated_content = content.replace('__REPLACE_ANIMALS_INFO__', output)

print(updated_content)

with open('animals.html', 'w') as file:
    file.write(updated_content)