import re

def alternate(s):
    s_unique = tuple(set(s))
    print(s_unique)
    max_len = 0
    for i in range(len(s_unique) - 1):
        for j in range(i + 1, len(s_unique)):
            prov_s = re.sub(rf'[^{s_unique[i]}|{s_unique[j]}]', '', s)
            for l in range(len(prov_s) - 1):
                if prov_s[l] == prov_s[l + 1]: break
                if l == len(prov_s) - 2 and len(prov_s) > max_len: max_len = len(prov_s)

    return max_len

if __name__ == '__main__':
    l = int(input().strip())
    s = input().strip()
    result = alternate(s)
    print(result)
