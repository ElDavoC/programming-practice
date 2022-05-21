def alt_char(s):
    if len(s) == 1: return 0

    prov = {'A':'B', 'B':'A'}
    if not prov[s[0]] in s: return len(s) - 1

    i, j = 0, 1;
    final = 0;
    while i < len(s) - 1:
        if prov[s[i]] == s[i + j]:
            i += j
            j = 1
        else:
            j += 1
            final += 1
            if i + j == len(s): break

    return final

def main():
    for _ in range(int(input().strip())):
        s = input().strip()
        result = alt_char(s)
        print(result)

if __name__ == '__main__':
    main()
