import os
import json
import logging

def setup_logging(log_file="app.log"):
    """Sets up logging for the application."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def load_json(file_path):
    """Loads a JSON file and returns its content as a dictionary."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from {file_path}: {e}")
        return {}

def save_json(file_path, data):
    """Saves a dictionary as a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Error writing JSON to {file_path}: {e}")

def validate_data(data, required_fields):
    """Validates if required fields exist in a given dictionary."""
    return all(field in data for field in required_fields)

def create_directory(directory_path):
    """Creates a directory if it does not exist."""
    os.makedirs(directory_path, exist_ok=True)

def read_file(file_path):
    """Reads the contents of a file and returns it as a string."""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Writes a string to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        logging.error(f"Error writing to file {file_path}: {e}")