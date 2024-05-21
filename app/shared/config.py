import os
import yaml

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
config_file_path = os.path.join(parent_dir, "shared", "config", "global_config.yaml")

with open(config_file_path, 'r') as f:
    config_data = yaml.safe_load(f)

environment = config_data['ENV']

env_file_path = os.path.join(parent_dir, "shared", "config", "env_"+environment+".yaml")

with open(env_file_path, 'r') as f:
    environment_config_data = yaml.safe_load(f)

config_data.update(environment_config_data)

config = dict(config_data)

def get_config():
    return config