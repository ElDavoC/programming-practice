def leap_year(n):
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)

def programmer_day(n):
    if n < 1918:
        return '12.09.' + str(n) if n % 4 == 0 else '13.09.' + str(n)
    elif n > 1918:
        return '12.09.' + str(n) if leap_year(n) else '13.09.' + str(n)
    else:
        return '26.09.1918'

if __name__ == '__main__':
    n = int(input().strip())
    result = programmer_day(n)
    print(result)
