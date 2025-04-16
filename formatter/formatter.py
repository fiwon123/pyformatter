from formatter.utils import get_dir_path, join_paths, create_dir, get_file_name
import json
import yaml

def format_json(filepath: str):
    with open(filepath, "r", encoding="utf-8") as file:
        content = json.loads(file.read())

    default_comma = ", "
    default_colon = " : "

    output = get_dir_path(filepath)
    output = join_paths(output, "output")
    create_dir(output)
    
    print(output)
    output = join_paths(output, get_file_name(filepath) + "_formatted.json")
    print(output)

    with open(output, "w", encoding="utf-8") as file:
        file.write(json.dumps(content, indent=4, separators=(default_comma, default_colon)))
    
    return True

def format_yaml(filepath: str):
    return True