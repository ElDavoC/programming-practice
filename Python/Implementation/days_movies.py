def beautiful_day(i, j, k):
    b_day = list(filter(lambda x:  abs(int(x) - int(x[::-1])) % k == 0, [str(n) for n in range(i, j + 1)]))
    return len(b_day)

if __name__ == '__main__':
    i, j, k = map(int, input().strip().split())
    result = beautiful_day(i, j, k)
    print(result)

    # Other Solutions
    beautifulDays = [1 for day in range(i, j + 1) if (day - int(str(day)[::-1])) % k == 0]
    print(sum(beautifulDays))
