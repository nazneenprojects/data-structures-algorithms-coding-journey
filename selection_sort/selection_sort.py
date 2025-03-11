""" "
Selection Sort
"""


# Find smallest item's index
def find_smallest(arr):
    # Assign first element from array as smallest
    smallest_num = arr[0]
    smallest_index = 0
    # Hence starts to iterate the array from 1 index
    for i in range(1, len(arr)):

        # check if its smallest that the stores smallest item , else replace it with current
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_index = i

    return smallest_index


# selection sort
def selection_sort(arr):

    # defines new array and one copied array
    newArray = []
    copiedArray = list(arr)

    # iterate through the copied array based on the current copied array length
    # in later steps , it will pop up item from copied array & it shortens the length
    for i in range(len(copiedArray)):

        smallest_index = find_smallest(copiedArray)
        # stores the result into new array
        newArray.append(copiedArray.pop(smallest_index))
    return newArray


if __name__ == "__main__":
    random_num = [12, 45, 12, 67, 12, 56, 999, 1, 34]
    result = selection_sort(random_num)
    print(f"Result of Selection Sort : , {result}")
