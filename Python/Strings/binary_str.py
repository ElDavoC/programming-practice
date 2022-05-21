def beautifulBinaryString(b):
    i = 0
    final = 0
    while i < len(b) - 3:
        prov = b.find('010', i)
        if prov != -1:
            final += 1
            i = prov + 3
            print(final, i)
        else:
            break

    return final

if __name__ == '__main__':
    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    print(result)
