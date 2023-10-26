import itertools
import time
from collections import defaultdict


def pcy(transactions, min_support):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1

        pairs_in_transaction = itertools.combinations(transaction, 2)
        for item1, item2 in pairs_in_transaction:
            bucket = (item1 + item2) % hash_bucket_size
            bucket_counts[bucket] += 1

    for item, count in item_counts.items():
        if count >= min_support:
            frequent_bucket = item % hash_bucket_size
            bit_vector[frequent_bucket] = 1

    frequent_items = {item for item, count in item_counts.items() if count / len(transactions) >= min_support}

    candidate_pairs = defaultdict(int)

    for transaction in transactions:
        item_pairs_in_transaction = itertools.combinations(transaction, 2)
        for item1, item2 in item_pairs_in_transaction:
            if item1 in frequent_items and item2 in frequent_items and bit_vector[(item1 + item2) % hash_bucket_size] == 1:
                candidate_pairs[(item1, item2)] += 1

    frequent_item_pairs = [pair for pair, count in candidate_pairs.items() if count / len(transactions) >= min_support]

    return frequent_item_pairs


if __name__ == "__main__":
    start = time.time()
    file_name = "retail.data" # Change as needed [CHECK README.TXT]
    min_support = 0.01 # Change as needed [CHECK README.TXT]
    hash_bucket_size = 997 # Change as needed [CHECK README.TXT]

    min_support_percentage = min_support * 100
    bucket_counts = [0] * hash_bucket_size
    bit_vector = [0] * hash_bucket_size
    transactions = []
    with open(file_name, 'r') as file:
        for line in file:
            transaction = list(map(int, line.strip().split()))
            transactions.append(transaction)

    frequent_item_pairs = pcy(transactions, min_support)
    file = "freq-itemsets_pcy_support" + str(min_support_percentage) + "%" + file_name + ".txt"
    with open(file, 'w') as f:
        for item_pair in frequent_item_pairs:
            f.write(str(item_pair) + '\n')
    end = time.time()
    total_time = end - start
    print("Execution time: ", end="")
    print('%.2f' % total_time + " seconds")
