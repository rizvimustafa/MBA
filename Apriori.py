import itertools
import time
from collections import defaultdict


def apriori(transactions, min_support):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1

    frequent_items = [item for item, count in item_counts.items() if count / len(transactions) >= min_support]

    candidate_pairs = set(itertools.combinations(frequent_items, 2))

    item_pair_counts = defaultdict(int)
    for transaction in transactions:
        for pair in candidate_pairs:
            if set(pair).issubset(transaction):
                item_pair_counts[pair] += 1

    frequent_item_pairs = [pair for pair in candidate_pairs if item_pair_counts[pair] / len(transactions) >= min_support]

    return frequent_item_pairs


if __name__ == "__main__":
    start = time.time()
    file_name = "retail.data" # Change as needed [CHECK README.TXT]
    min_support = 0.02 # Change as needed [CHECK README.TXT]

    min_support_percentage = min_support * 100
    transactions = []
    with open(file_name, 'r') as file:
        for line in file:
            transaction = list(map(int, line.strip().split()))
            transactions.append(transaction)

    frequent_item_pairs = apriori(transactions, min_support)
    file = "freq-itemsets_apriori_support" + str(min_support_percentage) + "%" + file_name + ".txt"
    with open(file, 'w') as f:
        for item_pair in frequent_item_pairs:
            f.write(str(item_pair) + '\n')
    end = time.time()
    total_time = end - start
    print("Execution time: ", end="")
    print('%.2f' % total_time + " seconds")
