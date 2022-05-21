def minimum_number(p):
    total = 0
    special_characters = "!@#$%^&*()-+"
    if not any(i.isupper() for i in p):
        total += 1

    if not any(i.islower() for i in p):
        total += 1

    if not any(i.isnumeric() for i in p):
        total += 1

    if not any(i in special_characters for i in p):
        total += 1

    if len(p) >= 6:
        return total
    else:
        return max((6 - len(p), total))

if __name__ == '__main__':
    n = int(input().strip())
    p = input().strip()
    result = minimum_number(p)
    print(result)
