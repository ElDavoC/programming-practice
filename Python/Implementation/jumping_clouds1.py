def jumps(clouds):
    i = 0
    j = 0
    while i < len(clouds) - 1:
        if i < len(clouds) - 2 and clouds[i + 2] != 1:
            i += 2
        else:
            i += 1

        j += 1

    return j

#   Recursive Solution
def jumpingOnClouds(c):
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1:
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])


if __name__ == '__main__':
    n = int(input().strip())
    clouds = [int(i) for i in input().split()]
    result = jumps(clouds)
    print(result)
