import os
import json


def read_json_file(filename):
    # Check if the analysis file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError(f'Input file "{filename}" not found in the specified working directory.')

    # Read the JSON file
    with open(filename, 'r') as file:
        try:
            variables = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"Error: Invalid JSON file '{filename}'")

    return variables


def write_json_file(outputfile: str, content):
    # Method for writing content as JSON to a file.
    # It takes the output file path and the content as input.
    try:
        with open(outputfile, 'w') as f:
            # Write the content as JSON to the output file
            json.dump(content, f, indent=4)

        print(f"Content written as JSON to '{outputfile}' successfully.")

    except IOError:
        print(f"Error: Failed to write content to '{outputfile}'.")
