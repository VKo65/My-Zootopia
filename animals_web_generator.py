import json


def load_data(file_path):
    """Takes data from json-file"""
    with open("animals_data.json", "r") as file:
        return json.load(file)


def read_template(template_path):
    """Takes the content of the html-file"""
    with open(template_path, "r") as file:
        return file.read()


def write_output(output_path, content):
    """writes the new generated html content in a file"""
    with open(output_path, "w") as file:
        file.write(content)


def serialize_animal(animal_obj):
    """generates a html for one single animal"""
    output = '<li class="cards__item">\n'
    try:
        output += f"<div class='card__title'>{animal_obj['name']}<br/>\n"
        output += "<p class='card__text'>\n"
        output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
        output += "</p>\n"
    except KeyError:
        output += "<p class='card__text'>Information missing</p>\n"
    output += "</li>\n"
    return output


def generate_animal_list(animals):
    """Use a loop to generate the html-string for all animals"""
    output = ""
    for animal in animals:
        output += serialize_animal(animal)
    return output


def main():
    """main function, to generate the new html"""

    animals = load_data("animals_data.json")
    html_content = read_template("animals_template.html")
    animal_list_html = generate_animal_list(animals)
    html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animal_list_html)

    # save the html-file with write_output-function
    write_output("animal.html", html_content)
    print("HTML-file was sucessfull generated.")


if __name__ == "__main__":
    main()