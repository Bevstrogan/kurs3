import pytest

from src.utils import *

@pytest.fixture
def class_fixture1():
    operation_test = Operation({'date': '2000-12-08T22:46:21.935582',
                                'operationAmount': {'amount': '41096.24',
                                                    'currency': {'name': 'USD', 'code': 'USD'}},
                                'description': 'Открытие вклада',
                                'to': 'Счет 90424923579946435907'})
    return operation_test

@pytest.fixture
def class_fixture2():
    operation_test_2 = Operation({'date': '2011-10-01T09:22:25.899614',
                                  'operationAmount': {'amount': '30153.72',
                                                      'currency': {'name': 'руб.', 'code': 'RUB'}},
                                  'description': 'Перевод организации',
                                  'from': 'Maestro 7810846596785568',
                                  'to': 'MasterCard 6783917276771847'})
    return operation_test_2

def test___repr__(class_fixture1):
    assert class_fixture1.__repr__() ==  "Operation('{'date': '2000-12-08T22:46:21.935582', " \
                                         "'operationAmount': {'amount': '41096.24', " \
                                         "'currency': {'name': 'USD', 'code': 'USD'}}, " \
                                         "'description': 'Открытие вклада', " \
                                         "'to': 'Счет 90424923579946435907'}')"
def test_date_format(class_fixture1):
    assert class_fixture1.date_format() == '08.12.2000'

def test_show_description(class_fixture1):
    assert class_fixture1.show_description() == 'Открытие вклада'

def test_show_from_none(class_fixture1):
    assert class_fixture1.show_from() == ''

def test_show_from_has(class_fixture2):
    assert class_fixture2.show_from() == 'Maestro 7810846596785568'

def test_censore_number_card(class_fixture2):
    assert class_fixture2.censore_number(class_fixture2.show_from()) == 'Maestro 7810 84** **** 5568'

def test_censore_number_account(class_fixture1):
    assert class_fixture1.censore_number(class_fixture1.show_to()) == "Счет **5907"

def test_last_five_operations():
    operations = [{"id": "1", "date": "01.01.2022", "state": "EXECUTED"},
                {},
                {"id": "2", "date": "03.01.2022", "state": "EXECUTED"},
                {"id": "3", "date": "06.01.2022", "state": "EXECUTED"},
                {"id": "4", "date": "10.01.2022", "state": "CANCELED"},
                {"id": "5", "date": "15.01.2022", "state": "EXECUTED"},
                {"id": "6", "date": "21.01.2022", "state": "EXECUTED"}]
    assert last_five_operations(operations) == [{'date': '21.01.2022', 'id': '6', 'state': 'EXECUTED'},
                                                {'date': '15.01.2022', 'id': '5', 'state': 'EXECUTED'},
                                                {'date': '06.01.2022', 'id': '3', 'state': 'EXECUTED'},
                                                {'date': '03.01.2022', 'id': '2', 'state': 'EXECUTED'},
                                                {'date': '01.01.2022', 'id': '1', 'state': 'EXECUTED'}]
