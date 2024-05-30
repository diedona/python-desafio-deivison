import funcs

print("this is the movable field:")
funcs.print_arr()

print()

while True:
    row = int(input("enter the row:"))
    column = int(input("enter the column:"))

    funcs.set_char_in_arr(row, column)

    print()

    funcs.print_arr()

    print()

    if funcs.check_winner():
        print("WINNER")
        break
