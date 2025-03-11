import time


def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


if __name__ == "__main__":


    start_timer = time.time()
    countdown(10)
    end_timer = time.time()

    print(f"Total time taken 2: {end_timer - start_timer} seconds")

    print("Time Complexity: O(n+1)  ---> O(n)")
    print("Space Complexity O(n+1)  -->  O(n)")

