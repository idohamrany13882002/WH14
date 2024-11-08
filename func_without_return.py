import statistics
from unittest.mock import sentinel


# exc.a
def my_ascending(a: int, b: int):
    """print the number in ascending order"""
    if a > b:
        print(b, a)
    else:
        print(a, b)


# exc.b
def my_details(a: str):
    print(a[0])
    print(a[len(a) // 2])
    print(a[-1])


# exc.c
def say_bool(a: bool):
    if a is True:
        print("yes")
    else:
        print("no")


# exc.d
def print_zugi(a: list[int]):
    for i in (a):
        if i % 2 == 0:
            print("even")
        else:
            print("odd")


# exc.e
def my_statistics(a: list[int]):
    if a is True:
        print(max(a))
        print(min(a))
        print(len(a))
        print(statistics.mean(a))
