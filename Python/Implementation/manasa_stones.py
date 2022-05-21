def stones(n, a, b):
    return ' '.join(map(str,sorted({x * a + (n - 1 - x) * b for x in range(n)})))


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, a, b = [int(input().strip()) for _ in range(3)]
        result = stones(n, a, b)
        print(result)
