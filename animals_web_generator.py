import json
def load_data(file_path):
    with open("animals_data.json", "r") as file:
        return json.load(file)

animals = load_data("animals_data.json")
for animal in range(len(animals)):
    try:
        print(f"\nName: {animals[animal]["name"]}")
        print(f"Diet: {animals[animal]["characteristics"]["diet"]}")
        print(f"Location: {animals[animal]["locations"][0]}")
        print(f"Type: {animals[animal]["characteristics"]["type"]}")
    except KeyError:
        pass

