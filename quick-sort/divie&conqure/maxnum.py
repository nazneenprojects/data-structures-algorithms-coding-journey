
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])

    return list[0] if list[0] > sub_max else sub_max


if __name__ == "__main__":
    print(max([12, 4455, 66, 56, 9, 0]))