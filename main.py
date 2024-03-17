from utils import print_transaction, sort_transactions, load_transactions


def main():
    file_path = 'transactions.json'
    transactions = load_transactions(file_path)
    sorted_transactions = sort_transactions(transactions)
    print_transaction(sorted_transactions)


if __name__ == "__main__":
    main()
