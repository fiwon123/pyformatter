# 💬 About

A simple command-line utility to format some files using Python and Typer. (.json, .yaml, .xml, .toml, ...)

## ✨ Features
- Pretty-print.
- Supports single or multiple files.
- Clean output using Rich.
- Simple CLI interface.

## 🚀 Installation
```bash
pip install .
```

For development:
```bash
pip install -e .
```

## 🛠 Usage
Use this following command to formmat any file available in the package:
```bash
formatter FILE_PATH
```

Use this command to list all availables parameters:
```bash
formatter --help
```


## 📁 Project Structure
```text
formatter-project/
├── formatter/                  # Main package
│   ├── formatters/
│   │   ├── base_formatter.py   
│   │   ├── json_formatter.py
│   │   ├── toml_formatter.py
│   │   ├── xml_formatter.py
│   │   └── yaml.formatter.py
│   ├──__init__.py              # Import formatters scripts
│   ├──__main__.py              # Use as a module
│   ├── cli.py                  # Entry point
│   ├── core.py                 # Proecess inputs
│   ├── formatter_logger.py    
│   ├── globals.py            
│   ├── registry.py             # Register all formatters to use in package
│   └── utils.py                # Used to manipulate string path, print and more
├── tests/                      # Unit tests
|   ├── tests_json/
│   ├── tests_toml/
│   ├── tests_xml/
│   ├── tests_yaml/
│   ├── test_json.py
│   ├── test_toml.py
│   ├── test_xml.py
│   └── test_yaml.py
├── LICENSE     
├── CHANGELOG.md
├── README.md
└── pyproject.toml              # Project metadata
```


## 🧪 Running Tests
```bash
pytest
```

## 🧾 License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.