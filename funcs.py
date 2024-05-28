def say_hi(name: str = "Unnamed"):
    print("Hello there, {}!".format(name))


def print_arr(arr: list[list[str]]) -> None:
    for column in arr:
        for row in column:
            print(row, end="")
        print()
