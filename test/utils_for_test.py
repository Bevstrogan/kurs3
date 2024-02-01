import datetime

def display_last_operations(file):
    ''' Функция отбирает из файла нужные операцци, затем
    их сортирует и выводит самые новые'''
    executed_operations = []
    for operation in file:
        if len(operation) == 0:
            continue
        if operation['state'] == 'EXECUTED':
            executed_operations.append(operation)
    sorted_operations = sorted(executed_operations, key=sorted_by_date, reverse=True)[:5]
    print(sorted_operations)
    return sorted_operations

def show_operations(sorted_operations):
    for operation in sorted_operations:
        if 'from' not in operation:
            print(f'''
{date_format(operation)} {operation['description']}
{censore_bank_account(operation)}  {amount_and_value(operation)}''')
        else:
            print(f'''{date_format(operation)} {operation['description']}
{censore_card_number(operation)} -> {censore_bank_account(operation)}
{amount_and_value(operation)}
''')
def sorted_by_date(op):
    ''' Функция нужна для сортировки по дате операции'''
    return datetime.datetime.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f')

def date_format(operation):
    '''Переводит дату в тип ДД.ММ.ГГГГ'''
    return f'{operation['date'][8:10]}.{operation['date'][5:7]}.{operation['date'][:4]}'

def censore_card_number(operation):
    '''Выводит название карты а также её скрытый номер за
     исключением первых 6 и последних 4 символов '''
    splited_from = operation['from'].split()
    card_name = splited_from[0]
    card_subname = '' # Перменная на случай если у карты название состоит из 2 слов
    if len(splited_from) == 3:
        card_subname = splited_from[1]
        card_number = splited_from[2]
        return f'{card_name} {card_subname} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    else:
        card_number = splited_from[1]
        return f'{card_name} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'

def censore_bank_account(operation):
    ''' Функция скрывает номер счета за исключением
    последних 4 символов'''
    return f'**{operation['to'][-4:]}'

def amount_and_value(operation):
    '''Функция выводит сумму и валюту операции'''
    amount = (operation['operationAmount'])['amount']
    value_currency = (operation['operationAmount'])['currency']
    value = value_currency['name']
    return f'{amount} {value}'

