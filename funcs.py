field_arr: list[list[str]] = [
    ["@", "@", "@", "@"],
    ["@", "@", "@", "@"],
    ["@", "@", "@", "@"],
]


def print_arr() -> None:
    for column in field_arr:
        for row in column:
            print(row, end="")
        print()


def set_char_in_arr(row: int, col: int, char: str = "x") -> None:
    field_arr[row][col] = char
