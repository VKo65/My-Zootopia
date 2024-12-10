import json
def load_data(file_path):
    with open("animals_data.json", "r") as file:
        return json.load(file)

animals = load_data("animals_data.json")

with open("animals_template.html", "r") as file:
    html_content = file.read()


def output_data():
    output = ""
    for animal in range(len(animals)):
        output += '<li class="cards__item">'
        try:
            output += f"\nName: {animals[animal]["name"]}<br/>\n"
            output += f"Diet: {animals[animal]["characteristics"]["diet"]}<br/>\n"
            output += f"Location: {animals[animal]["locations"][0]}<br/>\n"
            output += f"Type: {animals[animal]["characteristics"]["type"]}<br/>\n"
        except KeyError:
            pass
        output += "</li>"
    return output
#print(output_data())
html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output_data())
#print(html_content)

with open("animal.html", "w") as new_file:
    new_file.write(html_content)
