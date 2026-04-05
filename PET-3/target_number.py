def find_pair(arr, target):
    seen = {}  # Dictionary to store {value: index}

    for i in range(len(arr)):
        num = arr[i]
        complement = target - num

        # Check if the needed number to reach target is already in our map
        if complement in seen:
            # Print the index of the complement and the current index
            print(f"{seen[complement]},{i}")
            return

        # Store the current number and its index in the map
        seen[num] = i

    # If the loop finishes without returning, no pair was found
    print("-1")


# Test Cases
find_pair([0, -1, 2, -3, 1], -2)  # Output: 2,3
find_pair([1, -2, 1, 0, 5], 0)  # Output: -1
