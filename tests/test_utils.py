from utils import mask_account_number, mask_card_number, load_transactions, sort_transactions, \
    format_transactions


def test_mask_account_number():
    assert mask_account_number('7158300734726758') == '**6758'


def test_mask_card_number():
    assert mask_card_number('7158300734726758') == '7158 30** **** 6758'


def test_load_transactions():
    assert type(load_transactions('transactions.json')) is list


def test_sort_transactions(operations):
    assert type(sort_transactions(operations)) is list


def test_format_transactions(operations):
    assert type(format_transactions(operations)) is list

