def cut_sticks(arr):
    final = []
    while len(arr) > 0:
        final.append(len(arr))
        arr = list(map(lambda x: x - arr[0], arr))
        del arr[:arr.count(0)]

    return final


if __name__ == '__main__':
    n = int(input().strip())
    arr = sorted([int(i) for i in input().strip().split()])
    result = cut_sticks(arr)
    print(*result, sep = '\n')
