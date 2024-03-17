import json

from datetime import datetime


def load_transactions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    executed_transactions = [trans for trans in data if trans.get('state') == 'EXECUTED']
    return executed_transactions


def sort_transactions(transactions):
    transactions.sort(key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return transactions[:5]


def mask_card_number(card_number):
    if len(card_number) >= 10:
        return card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
    else:
        return card_number


def mask_account_number(account_number):
    if len(account_number) >= 4:
        return '**' + account_number[-4:]
    else:
        return account_number


def format_transactions(transactions):
    for t in transactions:
        t['date'] = datetime.strptime(t['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')

        from_acc = t.get('from', 'N/A').split()
        if 'Счет' in from_acc:
            t['from'] = 'Счет **' + from_acc[-1][-4:]

        else:
            t['from'] = ' '.join(from_acc[:-1]) + ' ' + mask_card_number(from_acc[-1:][0])

        to_acc = t.get('to', 'N/A').split()
        if 'Счет' in to_acc:
            t['to'] = 'Счет **' + to_acc[-1][-4:]

        else:
            t['to'] = ' '.join(to_acc[:-1]) + ' ' + mask_card_number(to_acc[-1:][0])

    return transactions


def print_transaction(transactions):
    for t in format_transactions(transactions):
        print(f"{t['date']} {t['description']}")
        print(f"{t['from']} -> {t['to']}")
        print(f"{t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")
