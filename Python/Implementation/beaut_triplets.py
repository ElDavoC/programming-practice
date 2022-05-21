def beautiful_triplets(arr, d):
    final = 0
    for i in arr:
        if i + d in arr and i + 2 * d in arr:
            final += 1

    return final

    # Other way
    return sum(1 for i in arr if i + d in arr and i + 2 * d in arr)


if __name__ == '__main__':
    n, d = map(int, input().strip().split())
    arr = [int(i) for i in input().strip().split()]
    result = beautiful_triplets(arr, d)
    print(result)
