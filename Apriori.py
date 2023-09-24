f = open("retail.data", "r")

d = dict()

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
        if integer in d:
            # Increment count of word by 1
            d[integer] = d[integer] + 1
        else:
            # Add the word to dictionary with count 1
            d[integer] = 1
        total = total + 1

support1 = 0.01
support2 = 0.02
for key in list(d.keys()):
    if d[key] / total < support1:
        del[d[key]]

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
print(total)


