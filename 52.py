# Check if a set is a subset of another set
# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}

# Check if set2 is a subset of set1
is_subset = set2.issubset(set1)

#OR
# Check if set2 is a subset of set1 using the <= operator
#is_subset = set2 <= set1

# Print the result
print(is_subset)
