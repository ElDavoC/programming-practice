def super_reduced(s):
    if s == '':
        return ''

    if len(s) == 1:
        return s

    if s[0] == s[1]:
        return super_reduced(s[2:])
    else:
        new_s = s[0] + super_reduced(s[1:])
        if new_s[0:1] == new_s[1:2]:
            return super_reduced(new_s)
        else:
            return new_s


if __name__ == '__main__':
    s = input().strip()
    result = super_reduced(s)
    print(result if len(result) > 0 else 'Empty String')
