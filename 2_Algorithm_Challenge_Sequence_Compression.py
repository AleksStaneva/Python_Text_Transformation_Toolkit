# 📉 Sequence Compression

# Step 1: Define the sequence
sequence = [1, 1, 1, 2, 2, 3, 1, 1]

# Step 2: Create an empty list to hold compressed result
compressed = []

# Step 3: Initialize variables to track the current number and count
# TODO: Set 'current' to the first element, and 'count' to 1
current_number = sequence[0]
counter = 1

# Step 4: Loop through the rest of the sequence
# TODO: If the number is the same as 'current', increase 'count'
# TODO: If different, append (current, count) to 'compressed', update 'current', reset 'count'

for number in sequence[1:]:
    if number == current_number:
        counter += 1
    else:
        compressed.append((current_number, counter))
        current_number = number
        counter = 1

# Step 5: Don’t forget to add the last group
# TODO: Append the final (current, count) to the result
compressed.append((current_number, counter))

# Step 6: Print the compressed sequence
# TODO: Output the 'compressed' list
print(compressed)