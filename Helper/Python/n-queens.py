def available(row, col):
    for k in range(row):
        if queen[k] is col or abs(queen[k] - col) is abs(k - row):
            return False
    return True


def find(row):
    global count, n, queen
    if row == n:
        count += 1
        print(queen)
    else:
        for col in range(n):
            if available(row, col):
                queen[row] = col
                find(row + 1)


def main():
    global count, n, queen
    n = 8
    queen = [-1] * n
    count = 0
    find(0)
    print(count)


main()
