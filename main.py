import json
import random
import os
import attr


@attr.s
class NameData:
    weights = attr.ib()
    prefix = attr.ib()
    middle = attr.ib()
    suffix = attr.ib()
    forbidden = attr.ib()


class NameGenerator:
    def __init__(self, data_directory):
        self.data_directory = data_directory

    def load_town_data(self, filename):
        """Load JSON data from a file."""
        with open(filename, "r") as file:
            data = json.load(file)
            return data

    def weighted_choice(self, items, weight):
        """Select an item from the list based on the given weight."""
        if random.random() < weight:
            return random.choice(items)
        return ""

    def generate_name(self, name_data):
        """Generate a name based on the given name data."""
        while True:
            parts = []

            # Select prefix based on weight
            prefix = self.weighted_choice(name_data.prefix, name_data.weights[0])
            if prefix:
                parts.append(prefix)

            # Select middle based on weight
            middle = self.weighted_choice(name_data.middle, name_data.weights[1])
            if middle:
                parts.append(middle)

            # Select suffix based on weight
            suffix = self.weighted_choice(name_data.suffix, name_data.weights[2])
            if suffix:
                parts.append(suffix)

            name = " ".join(parts).replace("  ", " ").title()

            if name and name not in name_data.forbidden:
                return name

    def select_name_type(self, town_data):
        """Prompt the user to select the type of name to generate."""
        types = list(town_data["types"].keys())
        print("Select the type of name to generate:")
        for idx, name_type in enumerate(types):
            print(f"{idx + 1}. {name_type.title()}")

        choice = int(input("Enter the number of your choice: ")) - 1
        if 0 <= choice < len(types):
            return types[choice]
        else:
            print("Invalid choice. Please try again.")
            return self.select_name_type(town_data)

    def select_json_file(self):
        """Prompt the user to select a JSON file to load."""
        files = [f for f in os.listdir(self.data_directory) if f.endswith(".json")]
        descriptions = []

        for filename in files:
            filepath = os.path.join(self.data_directory, filename)
            data = self.load_town_data(filepath)
            descriptions.append(data.get("description", "No description"))

        print("Select the JSON file to load:")
        for idx, desc in enumerate(descriptions):
            print(f"{idx + 1}. {desc}")

        choice = int(input("Enter the number of your choice: ")) - 1
        if 0 <= choice < len(files):
            return os.path.join(self.data_directory, files[choice])
        else:
            print("Invalid choice. Please try again.")
            return self.select_json_file()


if __name__ == "__main__":
    data_directory = "./data"
    name_generator = NameGenerator(data_directory)

    selected_file = name_generator.select_json_file()
    town_data = name_generator.load_town_data(selected_file)
    print(f"Loaded: {town_data['description']}")

    name_type = name_generator.select_name_type(town_data)
    name_data_dict = town_data["types"][name_type]

    # Convert the dictionary to a NameData object
    name_data = NameData(
        weights=name_data_dict["weights"],
        prefix=name_data_dict["prefix"],
        middle=name_data_dict["middle"],
        suffix=name_data_dict["suffix"],
        forbidden=name_data_dict["forbidden"],
    )

    for _ in range(10):  # Generate 10 random names
        print(name_generator.generate_name(name_data))
