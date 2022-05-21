import math

def workbook(arr, k):
    i = special = 0
    pages = 0
    while i < len(arr):
        pre = pages
        pages += math.ceil(arr[i] / k)
        n = 0
        for j in range(pre + 1, pages + 1):
            if j in range(n + 1, min(n + k + 1, arr[i] + 1)):
                special += 1

            n += k

        i += 1

    return special


if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    arr = [int(i) for i in input().strip().split()]
    result = workbook(arr, k)
    print(result)
