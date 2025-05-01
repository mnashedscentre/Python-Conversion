import pandas as pd
import json
import sys
import os

def convert_json_to_csv(json_file_path, csv_file_path=None):
    try:
        df = pd.read_json(json_file_path)
        
        # If csv_file_path is not provided, create one based on json filename
        if csv_file_path is None:
            csv_file_path = os.path.splitext(json_file_path)[0] + '.csv'
        
        # Convert to CSV
        df.to_csv(csv_file_path, index=False)
        print(f"Successfully converted {json_file_path} to {csv_file_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python json_to_csv_converter.py <json_file_path> [csv_file_path]")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    csv_file_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_json_to_csv(json_file_path, csv_file_path)