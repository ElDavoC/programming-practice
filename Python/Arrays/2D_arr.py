def hourglass_sum(arr):
    mega_max = None
    for i in range(1, len(arr) - 1):
        prov_max = max([sum(arr[i - 1][j - 1:j + 2] + [arr[i][j]] + arr[i + 1][j - 1:j + 2]) for j in range(1, len(arr[i]) - 1)])
        if mega_max is None or prov_max > mega_max:
            mega_max = prov_max

    return mega_max


if __name__ == '__main__':
    arr = [list(map(int, input().strip().split())) for _ in range(6)]
    result = hourglass_sum(arr)
    print(result)
