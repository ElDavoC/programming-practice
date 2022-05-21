def strange_counter(t):
    i = 1
    total = 3
    while t > total:
        i *= 2
        total += 3 * i
        
    return total - t + 1

# Better Solution
def strange_counter2(t):
    rem = 3
    while t > rem:
        t = t - rem
        rem *= 2

    return rem - t + 1



if __name__ == '__main__':
    t = int(input().strip())
    result = strange_counter(t)
    print(result)
