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
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['characteristics']['diet']}\n"
    output += f"Location: {animal['locations'][0]}\n"
    output += f"Type: {animal['characteristics'].get('type', 'Unknown')}\n"
    output += "\n"


#Replace placeholder with animal data
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new HTML file
with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html)

