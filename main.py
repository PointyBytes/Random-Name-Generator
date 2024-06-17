import json
import random


def load_town_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


def weighted_choice(items, weights):
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0
    for item, weight in zip(items, weights):
        if upto + weight >= r:
            return item
        upto += weight
    return items[-1]  # Fallback


def generate_name(town_data):
    while True:
        parts = []

        # Select prefix
        if town_data["weights"][0] > 0:
            parts.append(
                weighted_choice(
                    town_data["prefix"],
                    [town_data["weights"][0]] * len(town_data["prefix"]),
                )
            )

        # Select middle
        if town_data["weights"][1] > 0:
            parts.append(
                weighted_choice(
                    town_data["middle"],
                    [town_data["weights"][1]] * len(town_data["middle"]),
                )
            )

        # Select suffix
        if town_data["weights"][2] > 0:
            parts.append(
                weighted_choice(
                    town_data["suffix"],
                    [town_data["weights"][2]] * len(town_data["suffix"]),
                )
            )

        name = "".join(parts)

        if name not in town_data["forbidden"]:
            return name


if __name__ == "__main__":
    town_data = load_town_data("data/fantasy_towns.json")
    for _ in range(10):  # Generate 10 random names
        print(generate_name(town_data))
