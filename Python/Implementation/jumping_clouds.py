def jumps(k, clouds):
    if len(clouds) % k != 0:
        return 100 - len(clouds) - (clouds.count(1) * 2)
    else:
        return 100 - (len(clouds) // k) - sum([2 for i in range(0, len(clouds), k) if clouds[i] == 1])

if __name__ == '__main__':
    n, k = [int(i) for i in input().strip().split()]
    clouds = [int(i) for i in input().strip().split()]
    result = jumps(k, clouds)
    print(result)

    # Simplest solution
    energy = 100                #   initial energy
    i = k % n                   #   initial jump from 0
    energy -= c[i] * 2 + 1      #   initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1

    print(energy)
