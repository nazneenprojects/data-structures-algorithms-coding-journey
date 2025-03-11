def greet(name):
    print("hello, "+ name + "!")

    greet1(name)

    print("saying bye......")
    bye(name)


def greet1(name):
    print("How are you..?", name)

def bye(name):
    print("Bye Bye..", name)


if __name__ == "__main__":
    greet("Nazneen")