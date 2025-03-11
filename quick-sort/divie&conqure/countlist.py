def countListItems(arr):
    count = 0

    if arr == []:
        return 0

    return 1 + countListItems(arr[1:])

if __name__ == "__main__":
    print(countListItems([1, 2, 3, 4]))
