from formatter.utils import get_dir_path, join_paths, create_dir, get_file_name, error
import json
import yaml

def format_json(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = json.load(file)
    except json.JSONDecodeError as e:
        error(f"[ERROR] Invalid JSON: {e}")
        

    default_comma = ", "
    default_colon = " : "

    output = get_dir_path(filepath)
    output = join_paths(output, "output")
    create_dir(output)
    
    output = join_paths(output, get_file_name(filepath) + "_formatted.json")

    try:
        with open(output, "w", encoding="utf-8") as file:
            file.write(json.dumps(content, indent=4, separators=(default_comma, default_colon)))
    except TypeError as e:
        error(f"[ERROR] Unable to serialize data to JSON: {e}")
    
    return True

def format_yaml(filepath: str):
    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            content = yaml.safe_load(file)
    except yaml.YAMLError as e:
        error(f"[ERROR] Invalid YAML: {e}") 

    output = get_dir_path(filepath)
    output = join_paths(output, "output")
    create_dir(output)

    output = join_paths(output, get_file_name(filepath) + "_formatted.yaml")

    try:
        with open(output, "w", encoding="utf-8") as file:
            file.write(yaml.dump(content))
    except TypeError as e:
        error(f"[ERROR] Unable to serialize data to YAML: {e}")


    
    return True