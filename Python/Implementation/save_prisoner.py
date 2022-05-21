def prisoner(n, m, s):
    return n if (m + s - 1) % n == 0 else (m + s - 1) % n


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, m, s = [int(i) for i in input().strip().split()]
        result = prisoner(n, m, s)
        print(result)
