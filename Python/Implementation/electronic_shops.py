from itertools import product
from functools import reduce

def purchase(b, k, u, n, m):
    # My way
    try:
        return max(map(sum, filter(lambda x: b >= sum(x), product(k, u))))
    except:
        return -1

    # reduce solution
    return reduce(lambda x, y: sum(y) if (sum(y) <= b and sum(y) > x) else x, product(k, u), -1)

    # Other Way
    k.sort(reverse = True)
    u.sort()
    ms = -1
    i = j = 0
    while i < n:
        while j < m:
            if k[i] + u[j] > b:
                break
            if k[i] + u[j] > ms:
                ms = k[i] + u[j]
            j += 1
        i += 1
    return ms

if __name__ == '__main__':
    b, n, m = map(int, input().strip().split())
    keyboard, usb = (list(map(int, input().strip().split())) for _ in range(2))
    result = purchase(b, keyboard, usb, n, m)
    print(result)
