import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data  = load_data("animals_data.json")

# Read template file
with open("animals_template.html", "r", encoding="utf-8") as f:
    template = f.read()


# Generate string with animal information
output = ""
for animal in animals_data:
    output += "<li class='cards__item'>"
    output += f"<div class='card__title'>{animal['name']}</div>\n"
    output += f"<p class='card__text'>\n"
    output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    output += f"<strong>Type: </strong>{animal['characteristics'].get('type', 'Unknown')}<br/>\n"
    output += "</p>"
    output += "</li>\n"


#Replace placeholder with animal data
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new HTML file
with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html)

