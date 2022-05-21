def non_divisible(arr, k):
    range_k = [i for i in range(1, k)]
    remainders = [i % k for i in arr]
    for i in range(len(range_k) // 2):
        first = list(filter(lambda x: x != range_k[-i -1], remainders))
        second = list(filter(lambda x: x != range_k[i], remainders))
        remainders = first[:] if len(first) > len(second) else second[:]

    final = len(remainders)
    if remainders.count(0) > 1: final = final - remainders.count(0) + 1
    if k % 2 == 0 and remainders.count(k // 2) > 1: final = final - remainders.count(k // 2) + 1

    return final

if __name__ == '__main__':
    n, k = [int(i) for i in input().strip().split()]
    arr = [int(i) for i in input().strip().split()]
    result = non_divisible(arr, k)
    print(result)
