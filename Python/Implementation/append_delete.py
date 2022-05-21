def iguales(k, resta):
    if k % 2 == 0 and resta % 2 == 0:
        return True
    elif k % 2 != 0 and resta % 2 != 0:
        return True
    else:
        return False

def condition(s, t, k):
    combination = s + t[::-1]
    if combination == combination[::-1]:
        if len(s) - len(t) == 0:
            return 'Yes' if len(combination) <= k or k % 2 == 0 else 'No'
        else:
            return 'Yes' if iguales(k, abs(len(s) - len(t))) or len(combination) <= k else 'No'
    else:
        for i in range(len(combination) // 2):
            if combination[i] != combination[-1 - i]:
                return 'Yes' if k % len(combination[i:len(combination) - i]) == 0 or len(combination) <= k else 'No'


if __name__ == '__main__':
    s, t, k = input().strip(), input().strip(), int(input().strip())
    result = condition(s, t, k)
    print(result)
