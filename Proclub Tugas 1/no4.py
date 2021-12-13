rows = 5
a = 1

while a <= rows:
    if rows % 2 == 0 and a % 2 == 0 or rows % 2 != 0 and a % 2 != 0:
        print("  " * ((rows - a) // 2), "* " * a)
    else:
        print("  " * ((rows - a - 1) // 2) + " ", "* " * a)
    a += 1