
import time

# Factorial of 4 = 4 * 3* 2* 1


def factorial(num):
    if num == 1 :
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == "__main__":
    start = time.time()
    result = factorial(4)
    end = time.time()
    print("time taken :", end - start)
    print(result)