# JSON to CSV Converter

A Python script that converts JSON files to CSV format using pandas.

## Features

- Convert JSON files to CSV format
- Support for command-line usage
- Automatic output filename generation
- Error handling for file operations
- Can be used as a module in other Python scripts

## Requirements

- Python 3.x
- pandas

## Installation

1. Ensure you have Python 3.x installed
2. Install required packages:
```bash
pip install pandas
```

## Usage

### Command Line

```bash
python json_to_csv_converter.py <input_json_file> [output_csv_file]
```

- `input_json_file`: Path to the JSON file you want to convert (required)
- `output_csv_file`: Path for the output CSV file (optional)

If no output file is specified, the script will create a CSV file with the same name as the input file.

### As a Module

```python
from json_to_csv_converter import convert_json_to_csv

# Basic usage
convert_json_to_csv('input.json')

# Specify output file
convert_json_to_csv('input.json', 'output.csv')
```

## Example

```bash
python json_to_csv_converter.py data.json
# This will create data.csv in the same directory
```

## Error Handling

The script includes basic error handling for common issues such as:
- File not found
- Invalid JSON format
- Permission errors

Any errors will be printed to the console with a descriptive message.