def condition(b, i):
    if (i == 0 and b[i] != b[i + 1]) or ((i > 0 and i < len(b) - 1) and (b[i] != b[i - 1] and b[i] != b[i + 1])) or (i == len(b) - 1 and b[i] != b[i - 1]):
        return True
    else:
        return False

def happy_ladyBugs(b):
    b_set = list(set(b))
    if not all([b.count(i) > 1 for i in b_set if i != '_']):
        return 'NO'
    else:
        if  '_' in b_set:
            return 'YES'
        else:
            if len(b_set) == 1: return 'YES'
            for i in range(len(b)):
                if condition(b, i): return 'NO'

            return 'YES'


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        b = input().strip()
        # print(b, ''.join(sorted(b)))
        result = happy_ladyBugs(b)
        print(result)
