import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

'''<li class="cards__item">
  <div class="card__title">Wire Fox Terrier</div>
  <p class="card__text">
      <strong>Diet:</strong> Carnivore<br/>
      <strong>Location:</strong> North-America and Canada<br/>
      <strong>Type:</strong> mamal<br/>
  </p>
</li>'''

output = ""
for animal in animals_data:
    output += '<li class="cards__item">\n'
    if 'name' in animal:
        output += f"<div class='card__title'>{animal['name']}</div><br/>\n"
    output += "<p class='card__text'>\n"
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    if 'locations' in animal and animal['locations']:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    if 'characteristics' in animal and 'type' in animal['characteristics']:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
    output += '</p>\n'
    output += '</li>\n'

print(output)

with open('animals_template.html', 'r') as file:
    content = file.read()

#print(content)

updated_content = content.replace('__REPLACE_ANIMALS_INFO__', output)

#print(updated_content)

with open('animals.html', 'w') as file:
    file.write(updated_content)