import sys
import os
import json
import jsonschema
from jsonschema import validate

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)

    return input_file, output_file

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def validate_json(data):
    try:
        validate(instance=data, schema={"type": "object"})
    except jsonschema.exceptions.ValidationError as err:
        print(f"Invalid JSON data: {err}")
        sys.exit(1)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
        validate_json(data)
        print("JSON data loaded and validated.")

        if output_file.endswith('.json'):
            save_json(data, output_file)
            print(f"Data saved to {output_file}")
        else:
            print("Currently only .json output is supported.")
            sys.exit(1)
    else:
        print("Currently only .json input is supported.")
        sys.exit(1)