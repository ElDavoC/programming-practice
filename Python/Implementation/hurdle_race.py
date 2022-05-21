def potions(height, k):
    return 0 if max(height) <= k else max(height) - k

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    height = [int(i) for i in input().strip().split()]
    result = potions(height, k)
    print(result)
