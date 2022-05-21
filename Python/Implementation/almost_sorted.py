def swap(arr, i, ind):
    sort_arr = sorted(arr)
    prov = arr[:]
    prov[i], prov[ind] = prov[ind], prov[i]
    return True if prov == sort_arr else False

def cond_reverse(arr, i, ind):
    sort_arr = sorted(arr)
    prov = arr[:i] + arr[i:ind + 1][::-1] + arr[ind + 1:]
    return True if prov == sort_arr else False

def almostSorted(arr):
    sort_arr = sorted(arr)
    if arr == sort_arr: return 'yes'

    for i in range(len(arr)):
        if arr[i] != sort_arr[i]:
            ind = arr.index(sort_arr[i])
            if swap(arr, i, ind):
                return f'yes\nswap {i + 1} {ind + 1}'

            if cond_reverse(arr, i, ind):
                return f'yes\nreverse {i + 1} {ind + 1}'

            return 'no'



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = almostSorted(arr)
    print(result)
