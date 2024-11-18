from dotenv import load_dotenv
import yaml

def load_env():
    load_dotenv()

def load_params(file_path='params.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)