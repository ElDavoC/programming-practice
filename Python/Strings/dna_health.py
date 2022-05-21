def dna(gen, health, **kwargs):
    total = 0
    # final = dict(zip(health[kwargs['start']:kwargs['end'] + 1], gen[kwargs['start']:kwargs['end'] + 1]))
    print(kwargs)
    for i,g in enumerate(gen[kwargs['start']:kwargs['end'] + 1], kwargs['start']):
        pos = kwargs['word'].find(g)
        while pos != -1:
            total += health[i]
            pos += 1
            if pos == len(kwargs['word']): break
            pos = kwargs['word'].find(g, pos)
    # for k,v in final.items():
    #     pos = kwargs['word'].find(v)
    #     while pos != -1:
    #         total += k
    #         pos += 1
    #         if pos == len(kwargs['word']): break
    #         pos = kwargs['word'].find(v, pos)

    return total

def main():
    n = int(input())
    g = input().strip().split()
    h = [int(i) for i in input().strip().split()]
    final = dict()
    for _ in range(int(input())):
        fld = input().strip().split()
        result = dna(g, h, start=int(fld[0]), end=int(fld[1]), word=fld[2])
        if final.get('hst', None) is None or final['hst'] < result:
            final['hst'] = result

        if final.get('uhst', None) is None or final['uhst'] > result:
            final['uhst'] = result

    print(final['uhst'], final['hst'])


if __name__ == "__main__":
    main()
