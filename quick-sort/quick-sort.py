"""
Quick Sort using Divide And Conquer
"""

def quick_sort(arr):
    if len(arr) < 2:
        return arr  # Base case: already sorted

    pivot = arr[0]  # Choosing the first element as pivot
    left_subarray = [i for i in arr[1:] if i <= pivot]  # Elements less than or equal to pivot
    right_subarray = [i for i in arr[1:] if i > pivot]  # Elements greater than pivot

    return quick_sort(left_subarray) + [pivot] + quick_sort(right_subarray)  # Recursively sorting both halves

if __name__ == "__main__":
    arr = [12, 34, 56, 2, 1, 90, 234, 67]
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)
