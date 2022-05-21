import math

# def space_stations(arr, n):
#     long_dist = max([arr[i + 1] - arr[i] - 1 for i in range(len(arr) - 1)])
#     return math.ceil(long_dist / 2)

def space_stations(arr, n):
    maxd = max(arr[0], n - 1 - arr[-1])
    for i in range(len(arr) - 1):
        maxd = max((arr[i + 1] - arr[i]) // 2, maxd)

    return maxd


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    arr = sorted([int(i) for i in input().strip().split()])
    if n == m:
        print(0)
    else:
        result = space_stations(arr, n)
        print(result)
