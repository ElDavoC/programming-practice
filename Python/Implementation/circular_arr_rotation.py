from collections import deque

if __name__ == '__main__':
    n, k, q = [int(i) for i in input().strip().split()]
    arr = deque(int(i) for i in input().strip().split())
    arr.rotate(k)
    [print(arr[int(input().strip())]) for _ in range(q)]
