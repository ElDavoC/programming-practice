from string import ascii_lowercase as aski

def caesar_cipher(s, k):
    final = []
    for l in s:
        l_prov = l.lower()
        if l_prov in aski:
            pos = (aski.index(l_prov) + k) % 26
            final.append(aski[pos].upper() if l.isupper() else aski[pos])
        else:
            final.append(l)

    return ''.join(final)

if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesar_cipher(s, k)
    print(result)
