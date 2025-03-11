


def countdown(i):
    print(i)
    while True:
        if i > 0:
            break


    countdown(i-1)


if __name__ == "__main__":
    countdown(10)