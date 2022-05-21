import re
def hacker_sub(s):
    pos = 0
    for i in 'hackerrank':
        if s.find(i, pos) == -1: return 'NO'
        pos = s.find(i, pos) + 1

    return 'YES'

# REGEX solution
def hacker_re(s):
    return 'YES' if re.search(r'.*?'.join(list('hackerrank')), s) else 'NO'

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        s = input().strip()
        result = hacker_re(s)
        print(result)
