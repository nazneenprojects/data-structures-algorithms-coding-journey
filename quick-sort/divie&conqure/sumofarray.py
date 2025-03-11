def sum(arr):
    total = 0

    for i in arr:
        total += i
    return total

# def sum_dc(arr):
#     total = 0
#     if len(arr) == 0:
#         return 0
#     else:
#         total = arr[i] + sum(arr)

def sum_dc(list):
    if list == []:
        return 0
    return list[0] + sum_dc(list[1:])


if __name__ == "__main__":
    print(sum([1, 2, 3, 4]))
    print(sum_dc([1, 2, 3, 4]))