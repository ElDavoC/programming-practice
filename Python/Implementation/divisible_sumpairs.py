def divisible(arr, k):
    return sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if (arr[i] + arr[j]) % k == 0)

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    result = divisible(arr, k)
    print(result)
