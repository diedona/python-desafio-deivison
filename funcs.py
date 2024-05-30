field_arr: list[list[str]] = [
    ["@", "@", "@"],
    ["@", "@", "@"],
    ["@", "@", "@"],
]


def print_arr() -> None:
    for row in field_arr:
        for column in row:
            print(column, end="")
        print()


def set_char_in_arr(row: int, col: int, char: str = "x") -> None:
    if row > len(field_arr) - 1:
        print("this row is not rolling...")
        return

    if col > len(field_arr[row]) - 1:
        print("this col is not rolling...")
        return

    field_arr[row][col] = char


def check_winner() -> bool:
    for row in range(0, 3):
        for col in range(0, 3):

            # check winner by row
            if (
                field_arr[row][0] == "x"
                and field_arr[row][1] == "x"
                and field_arr[row][2] == "x"
            ):
                return True

            # check winner by column
            if (
                field_arr[0][col] == "x"
                and field_arr[1][col] == "x"
                and field_arr[2][col] == "x"
            ):
                return True

    # center cross case
    if field_arr[1][1] == "x":
        return (field_arr[0][0] == "x" and field_arr[2][2] == "x") or (
            field_arr[0][2] == "x" and field_arr[2][0] == "x"
        )

    return False
