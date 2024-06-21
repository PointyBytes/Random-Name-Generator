# Random Name Generator
I always run into projects where I am in need of a list of random names. Please feel free to add to this or add changes to it as you see fit. My plan is to make a library of lists made up of segments that can be combined together.

## Adding a New JSON File

To add a new set of name data for the name generator, follow these steps:

1. Create a new JSON file in the `/data` directory.
2. Use the following template to structure your JSON file:

```json
{
  "description": "Your Description Here",
  "types": {
    "your_type": {
      "weights": [0.5, 0.5, 0.5],
      "prefix": ["Your", "List", "Of", "Prefixes"],
      "middle": ["Your", "List", "Of", "Middles"],
      "suffix": ["Your", "List", "Of", "Suffixes"],
      "forbidden": ["ListOfForbiddenNames"]
    }
  }
}
```

3. Save the file with a descriptive name, such as `fantasy_names.json` or `sci-fi_names.json`.


## License

This project is open source and available under the **GNU GPL v3.0 or later**. You can find the full license text in the [LICENSE](LICENSE) file within this repository.