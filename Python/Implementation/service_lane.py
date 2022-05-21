def serviceLane(arr, cases):
    return min(arr[cases[0]:cases[1] + 1]) 


if __name__ == '__main__':
    n, t = map(int, input().strip().split())
    arr = [int(i) for i in input().strip().split()]
    for _ in range(t):
        case = list(map(int, input().strip().split()))
        result = serviceLane(arr, case)
        print(result)
