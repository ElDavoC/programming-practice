def rotleft(arr, d):
    mod = d % len(arr)
    return arr[mod:] + arr[:mod]

if __name__ == '__main__':
    n, d = map(int, input().strip().split())
    arr = [int(i) for i in input().strip().split()]
    result = rotleft(arr, d)
    print(*result)
