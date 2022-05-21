def pair_socks(arr):
    sock_set = set(arr)
    return sum([arr.count(i) // 2 for i in sock_set])


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = pair_socks(arr)
    print(result)
