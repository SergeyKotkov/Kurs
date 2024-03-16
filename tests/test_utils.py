from utils import sort_transactions


def test_sort_transactions():
    assert sort_transactions("2018-06-30T02:08:58.425572") == "30.06.2018"
