import csv
import json
import re
from dateutil import parser as date_parser

def detect_and_convert_type(value_str):
    """Detect and convert a string to its appropriate Python type."""
    value_str = value_str.strip()

    # Integer
    if re.match(r'^[-+]?\d+$', value_str):
        return int(value_str)

    # Float
    if re.match(r'^[-+]?\d*\.\d+$', value_str):
        return float(value_str)

    # Boolean
    if value_str.lower() == 'true':
        return True
    if value_str.lower() == 'false':
        return False

    # List
    if value_str.startswith('[') and value_str.endswith(']'):
        try:
            return json.loads(value_str)
        except json.JSONDecodeError:
            pass

    # Dictionary
    if value_str.startswith('{') and value_str.endswith('}'):
        try:
            return json.loads(value_str)
        except json.JSONDecodeError:
            pass

    # Date
    try:
        return date_parser.parse(value_str)
    except ValueError:
        pass

    # String (default)
    return value_str

def process_csv_data(file_path, column_types=None):
    """Process CSV data with column type conversions."""
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            converted_row = []
            for i, value in enumerate(row):
                if column_types and i < len(column_types):
                    if column_types[i] == 'int':
                        converted_row.append(int(value))
                    elif column_types[i] == 'float':
                        converted_row.append(float(value))
                    elif column_types[i] == 'bool':
                        converted_row.append(value.lower() == 'true')
                    elif column_types[i] == 'date':
                        converted_row.append(date_parser.parse(value))
                    else:
                        converted_row.append(value)
                else:
                    converted_row.append(detect_and_convert_type(value))
            data.append(converted_row)
    return header, data

def parse_config_string(config_text):
    """Parse configuration text into a dictionary with proper types."""
    config = {}
    for line in config_text.splitlines():
        line = line.strip()
        if not line:
            continue

        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()
        config[key] = detect_and_convert_type(value)
    return config

def transform_dataset(data, transformation_rules):
    """Apply type transformations to a dataset based on rules."""
    transformed_data = []
    for row in data:
        new_row = list(row)  # Create a mutable copy
        for rule in transformation_rules:
            try:
                index = rule['index']
                transformation_type = rule['type']

                if 0 <= index < len(new_row):
                    if transformation_type == 'int':
                        new_row[index] = int(new_row[index])
                    elif transformation_type == 'float':
                        new_row[index] = float(new_row[index])
                    elif transformation_type == 'bool':
                        new_row[index] = bool(new_row[index])
                    # Add other transformations as needed
            except (ValueError, IndexError) as e:
                print(f"Transformation error: {e}")
        transformed_data.append(new_row)
    return transformed_data