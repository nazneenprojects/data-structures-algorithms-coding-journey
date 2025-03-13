"""
Here’s the time complexity for each operation in binary search:

Splitting the array in half: This takes O(1) time.
Throwing away one half: This also takes O(1) time.
Calling binary search on the remaining half: Since we're halving the problem size each time, the recurrence is O(logn).
Thus, the overall time complexity of binary search is O(logn).
"""



def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Found the target
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # Search right half
    else:
        return binary_search(arr, target, low, mid - 1)  # Search left half

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)
print("Index of target:", result)  # Output: Index of target: 3
