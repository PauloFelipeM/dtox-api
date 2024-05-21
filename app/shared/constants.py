import os
import yaml

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
constants_file_path = os.path.join(parent_dir, "shared", "config", "constants.yaml")

with open(constants_file_path, 'r') as f:
    constants = yaml.safe_load(f)

def get_constants():
    return constants