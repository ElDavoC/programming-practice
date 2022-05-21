def extraLongFactorials(n):
    final = n
    for i in range(n - 1, 0, -1):
        final *= i
    
    print(final)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
