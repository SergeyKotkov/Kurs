from utils import mask_account_number, mask_card_number, load_transactions


def test_mask_account_number():
    assert mask_account_number('7158300734726758') == '****6758'

def test_mask_card_number():
    assert mask_card_number('7158300734726758') == '715830******6758'

def test_load_transactions():
    assert load_transactions is not None
    assert load_transactions() >= 0


