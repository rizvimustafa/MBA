def generate_candidates(itemset, k):
    candidates = set()
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            union = itemset[i] | itemset[j]
            if len(union) == k:
                candidates.add(union)
    return list(candidates)


def prune_candidates(candidates, prev_frequent_sets):
    pruned_candidates = []
    for candidate in candidates:
        is_valid = True
        for subset in candidate:
            if frozenset(subset) not in prev_frequent_sets:
                is_valid = False
                break
        if is_valid:
            pruned_candidates.append(candidate)
    return pruned_candidates


def apriori_algorithm(transactions, min_support):
    transaction_list = list(transactions)
    num_transactions = len(transaction_list)
    k = 1
    frequent_itemsets = []

    # Create a dictionary to store item counts
    item_counts = {}
    for transaction in transaction_list:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    # Find frequent 1-itemsets
    frequent_1_itemsets = {frozenset([item]): count / num_transactions for item, count in item_counts.items() if
                           count / num_transactions >= min_support}
    frequent_itemsets.append(frequent_1_itemsets)

    while frequent_itemsets[k - 1]:
        k += 1
        candidates = generate_candidates(list(frequent_itemsets[k - 2].keys()), k)
        candidate_counts = {candidate: 0 for candidate in candidates}

        for transaction in transaction_list:
            for candidate in candidates:
                if set(candidate).issubset(set(transaction)):
                    candidate_counts[frozenset(candidate)] += 1

        frequent_itemsets_k = {itemset: count / num_transactions for itemset, count in candidate_counts.items() if
                               count / num_transactions >= min_support}
        frequent_itemsets.append(frequent_itemsets_k)

    return frequent_itemsets[:-1]


# Sample dictionary of keys and their counts
f = open("retail.data", "r")

data_dict = dict()

total = 0
# Loop through each line of the file
next(f)
for line in f:
    # Remove the leading spaces and newline character
    line = line.strip()
    # Split the line into words
    integers = line.split(" ")

    # Iterate over each word in line
    for integer in integers:
        # Check if the word is already in dictionary
        if integer in data_dict:
            # Increment count of word by 1
            data_dict[integer] = data_dict[integer] + 1
        else:
            # Add the word to dictionary with count 1
            data_dict[integer] = 1

# Convert the dictionary into a list of transactions
transactions = [[key] * count for key, count in data_dict.items()]

# Define the minimum support threshold (adjust as needed)
min_support = 0.2  # This means an itemset should appear in at least 30% of transactions

# Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori_algorithm(transactions, min_support)

# Print the frequent itemsets
for k, itemsets in enumerate(frequent_itemsets):
    print(f"Frequent {k + 1}-itemsets:")
    for itemset, support in itemsets.items():
        print(f"Itemset: {set(itemset)}, Support: {support:.2f}")
