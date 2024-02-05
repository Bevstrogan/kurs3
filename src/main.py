from src.utils import *

if __name__ == '__main__':
    loadet_operations = load_operations('operations.json')
    sorted_operations = last_five_operations(loadet_operations)
    for element in sorted_operations:
        operation = Operation(element)
        print(f'''
{operation.date_format()} {operation.show_description()}
{operation.censore_number(operation.show_from())} -> {operation.censore_number(operation.show_to())}
{operation.amount()}''')