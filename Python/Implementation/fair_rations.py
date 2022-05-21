def fairRations(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0: continue
        arr[i] += 1
        if i < len(arr) - 1:
            arr[i + 1] += 1
        else:
            arr[i - 1] += 1

        total += 2

    return total if all(map(lambda x: x % 2 == 0, arr)) else 'NO'


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    result = fairRations(arr)
    print(result)
