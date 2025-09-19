import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data  = load_data("animals_data.json")

# Read template file
with open("animals_template.html", "r", encoding="utf-8") as f:
    template = f.read()



def serialize_animal(animal_obj):
    """Serializes an animal object"""
    output = ""
    output += "<li class='cards__item'>"
    output += f"<div class='card__title'>{animal_obj['name']}</div>\n"
    output += "<div class='card__text'>\n"
    output += "<ul>\n"
    output += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n"
    output += f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n"
    output += f"<li><strong>Type: </strong>{animal_obj['characteristics'].get('type', 'Unknown')}</li>\n"
    output += "</ul>\n"
    output += "</div>\n"
    output += "</li>\n"
    return output



output = ""
for animal in animals_data:
    output += serialize_animal(animal)






#Replace placeholder with animal data
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new HTML file
with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html)

