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
        try:
            output += f"\nName: {animals[animal]["name"]}\n"
            output += f"Diet: {animals[animal]["characteristics"]["diet"]}\n"
            output += f"Location: {animals[animal]["locations"][0]}\n"
            output += f"Type: {animals[animal]["characteristics"]["type"]}\n"
        except KeyError:
            pass
    return output
#print(output_data())
html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output_data())
#print(html_content)

with open("animal.html", "w") as new_file:
    new_file.write(html_content)
