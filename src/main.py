import json
from src.utils import display_last_operations

''' Главный код функции '''
if __name__ == "__main__":
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        file = json.load(json_file)
        display_last_operations(file)