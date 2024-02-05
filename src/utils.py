import datetime
import json

class Operation():
    def __init__(self, operation):
        self.operation = operation

    def __repr__(self):
        return f'{self.operation}'

    def show_description(self):
        return self.operation['description']

    def show_from(self):
        if "from" in self.operation.keys():
            return self.operation['from']
        else:
            return ''

    def show_to(self):
        return self.operation["to"]

    def date_format(self):
        """
        Выводит дату
        """
        operation_date_str = self.operation["date"]
        operation_date = datetime.datetime.strptime(operation_date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return operation_date.strftime("%d.%m.%Y")

    def censore_number(self, account):
        account = account.split(" ")
        account_number = account[-1]
        account.pop(len(account) - 1)
        account_name = " ".join(account)
        if "Счет" in account:
            return f"{account_name} **{account_number[16:20]}"
        else:
            return f"{account_name} {account_number[0:4]} {account_number[4:6]}** **** {account_number[12:16]}"

    def amount(self):
        return f'{self.operation["operationAmount"]["amount"]} {self.operation["operationAmount"]["currency"]["name"]}'


def load_operations(path):
    with open(path, "r", encoding='utf8') as file:
        operations = json.load(file)
        return operations

def last_five_operations(operations):
    oper_list_clean = [opr for opr in operations if opr != {} and opr["state"] == "EXECUTED"]
    oper_list_clean.sort(key=lambda dictionary: dictionary["date"], reverse=True)
    last_five_oper = oper_list_clean[0:5]
    return last_five_oper