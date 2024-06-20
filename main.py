import json
import random


def load_town_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


def weighted_choice(items, weight):
    if random.random() < weight:
        return random.choice(items)
    return ""


def generate_name(name_data):
    while True:
        parts = []

        # Select prefix based on weight
        prefix = weighted_choice(name_data["prefix"], name_data["weights"][0])
        if prefix == "":
            pass
        else:
            parts.append(prefix)

        # Select middle based on weight
        middle = weighted_choice(name_data["middle"], name_data["weights"][1])
        if middle == "":
            pass
        else:
            parts.append(middle)

        # Select suffix based on weight
        suffix = weighted_choice(name_data["suffix"], name_data["weights"][2])
        if suffix == "":
            pass
        else:
            parts.append(suffix)

        name = "".join(parts)
        name = name.replace("  ", " ")
        name = name.title()

        if name and name not in name_data["forbidden"]:
            return name


def select_name_type(town_data):
    types = list(town_data["types"].keys())
    print("Select the type of name to generate:")
    for idx, name_type in enumerate(types):
        print(f"{idx + 1}. {name_type.title()}")

    choice = int(input("Enter the number of your choice: ")) - 1
    if 0 <= choice < len(types):
        return types[choice]
    else:
        print("Invalid choice. Please try again.")
        return select_name_type(town_data)


if __name__ == "__main__":
    town_data = load_town_data("data/towns.json")
    name_type = select_name_type(town_data)
    name_data = town_data["types"][name_type]

    for _ in range(10):  # Generate 10 random names
        print(generate_name(name_data))
