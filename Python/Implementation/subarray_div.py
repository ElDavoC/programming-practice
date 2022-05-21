def chocolate(arr, d, m):
    #comb = 0
    #for i in range(len(arr) - m):
        #if sum(arr[i:i + m]) != d: continue
    #    comb += 1

    #return comb
    return sum([1 for i in range(len(arr) - m + 1) if sum(arr[i:i + m]) == d])

if __name__ == '__main__':
    n = int(input().strip())
    bar_ch = list(map(int, input().strip().split()))
    d, m = map(int, input().strip().split())

    result = chocolate(bar_ch, d, m)
    print(result)
