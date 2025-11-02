array = [2, 4, 5000, 783, 48, 3, 93]
target = 5002

# Step 1: Sort the array while keeping track of original indices
indexed_array = list(enumerate(array))
indexed_array.sort(key=lambda x: x[1])  # Sort by value

Left = 0
Right = len(indexed_array) - 1

while Left < Right:
    sum_val = indexed_array[Left][1] + indexed_array[Right][1]
    if sum_val == target:
        print("Found at indices:", indexed_array[Left][0], "and", indexed_array[Right][0])
        break
    elif sum_val < target:
        Left += 1
    else:
        Right -= 1
        print("hey")
        print("hey")