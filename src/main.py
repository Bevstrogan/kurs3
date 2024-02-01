import json
from src.utils import display_last_operations, show_operations

''' Главный код функции '''
if __name__ == "__main__":
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        file = json.load(json_file)
        last_operations = display_last_operations(file)
        show_operations(last_operations)