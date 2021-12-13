rows = 5

for i in range(rows, 0, -1):
    if rows % 2 != 0 and i % 2 == 0 or rows % 2 == 0 and i % 2 != 0:
        print("  " * ((rows - i) // 2) + " ", "* " * i)
    else:
        print("  " * ((rows - i) // 2), "* " * i)
