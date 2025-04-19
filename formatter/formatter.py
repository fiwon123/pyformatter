from formatter.utils import get_dir_path, join_paths, create_dir, get_file_name, print_error, print_msg, print_warning
import json
import yaml

def check_json(filepath: str):
    print_msg("Checking JSON...")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content_original = file.read()
        with open(filepath, "r", encoding="utf-8") as file:
            content = json.load(file)
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON: {e}")

    default_comma = ", "
    default_colon = " : "

    preview = json.dumps(content, indent=4, separators=(default_comma, default_colon))
    if (content_original != preview):
        print_warning("JSON is not correct formatted. But syntax is OK.")
        return False
    
    print_msg("JSON is already formatted.", True)
    return True


def dry_run_json(filepath: str):
    print_msg("JSON Preview:")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = json.load(file)
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON: {e}")
        
    default_comma = ", "
    default_colon = " : "

    try:
        print_msg(json.dumps(content, indent=4, separators=(default_comma, default_colon)))
    except TypeError as e:
        print_error(f"Unable to serialize data to JSON: {e}")
    
    return True
    

def format_json(filepath: str):
    print_msg("Formatting JSON...")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = json.load(file)
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON: {e}")
        
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
        print_error(f"Unable to serialize data to JSON: {e}")

    print_msg("JSON completed.", True)
    
    return True

def check_yaml(filepath: str):
    print_msg("Checking YAML...")

    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            content_original = file.read()
        with open(filepath, "r", encoding="UTF-8") as file:
            content = yaml.safe_load(file)
    except yaml.YAMLError as e:
        print_error(f"Invalid YAML: {e}") 

    preview = yaml.dump(content)
    if (content_original != preview):
        print_warning("YAML is not correct formatted. But syntax is OK.")
        return False
    
    print_msg("YAML is already formatted.", True)
    return True

def dry_run_yaml(filepath: str):
    print_msg("YAML preview:")

    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            content = yaml.safe_load(file)
    except yaml.YAMLError as e:
        print_error(f"Invalid YAML: {e}") 


    try:
        print_msg(yaml.dump(content))
    except TypeError as e:
        print_error(f"Unable to serialize data to YAML: {e}")
    
    return True

def format_yaml(filepath: str):
    print_msg("Formatting YAML...")

    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            content = yaml.safe_load(file)
    except yaml.YAMLError as e:
        print_error(f"Invalid YAML: {e}") 

    output = get_dir_path(filepath)
    output = join_paths(output, "output")
    create_dir(output)

    output = join_paths(output, get_file_name(filepath) + "_formatted.yaml")

    try:
        with open(output, "w", encoding="utf-8") as file:
            file.write(yaml.dump(content))
    except TypeError as e:
        print_error(f"Unable to serialize data to YAML: {e}")

    print_msg("YAML completed.", True)
    
    return True