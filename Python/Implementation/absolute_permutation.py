def absolute_permutation(n, k):
    if k >= n : return [-1]
    prov = list(range(1, n + 1))
    if k == 0 : return prov

    final = []
    i = 0
    while i < len(prov) - 1:
        final += prov[i + k:i + 2 * k] + prov[i:i + k]
        i += 2 * k

    return final if all([abs(i[1]-i[0]) == k for i in enumerate(final, 1)]) else [-1]


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = map(int, input().strip().split())
        result = absolute_permutation(n, k)
        print(*result)
