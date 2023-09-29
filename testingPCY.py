# Step 1: Read the dataset from the .data file into a dictionary
transactions = {}
with open('retail.data', 'r') as file:
    for line in file:
        transaction = list(map(int, line.strip().split()))  # Convert to integers
        transactions[len(transactions)] = transaction  # Use a unique identifier as the key

# Step 2: Create a hash table (hash bucket) for item pair counts
hash_table = {}

# Step 3: First Pass - Count individual items and hash pair counts
for transaction in transactions.values():
    # Count individual items (1-itemsets)
    for item in transaction:
        if item in hash_table:
            hash_table[item] += 1
        else:
            hash_table[item] = 1

    # Hash item pairs and update the hash table
    for i in range(len(transaction)):
        for j in range(i + 1, len(transaction)):
            item1, item2 = transaction[i], transaction[j]
            pair = (item1, item2)
            hash_value = hash(pair) % 10000  # You can adjust the hash function and size
            if hash_value in hash_table:
                hash_table[hash_value] += 1
            else:
                hash_table[hash_value] = 1

#print(hash_table)
# Step 4: Determine the threshold for frequent n-itemsets
total_transactions = len(transactions)
min_support_percentage = 1  # 1% support threshold
threshold = total_transactions * (min_support_percentage / 100)

# Step 5: Generate candidate n-itemsets (for n > 2)
n = 3  # Example for generating frequent 3-itemsets
candidate_n_itemsets = {}
for pair, count in hash_table.items():
    if count >= threshold:
        for item in hash_table.keys():
            if not item == pair:
                candidate = tuple(sorted(pair + item))
                candidate_n_itemsets[candidate] = 0  # Initialize count to 0

# Step 6: Second Pass - Count frequent n-itemsets
for transaction in transactions.values():
    for itemset in candidate_n_itemsets.keys():
        if all(item in transaction for item in itemset):
            candidate_n_itemsets[itemset] += 1

# Filter frequent n-itemsets based on support threshold
frequent_n_itemsets = {itemset: count for itemset, count in candidate_n_itemsets.items() if count >= threshold}

# Print frequent n-itemsets
for itemset, count in frequent_n_itemsets.items():
    print(itemset, count)
