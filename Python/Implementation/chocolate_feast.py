import math

def chocolateFeast(n, c, m):
    if n < c: return 0
    total = bars = math.floor(n / c)
    while bars / m >= 1:
        total += math.floor(bars / m)
        # bars = bars - (m * math.floor(bars / m)) + math.floor(bars / m)
        bars += math.floor(bars / m) * (1 - m)

    return total


if __name__ == '__main__':
    for _ in range(int(input())):
        n, c, m = map(int, input().strip().split())
        result = chocolateFeast(n, c, m)
        print(result)
