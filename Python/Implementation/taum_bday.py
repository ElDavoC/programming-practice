def taum_bday(b, w, bc, wc, z):
    basic = b * bc + w * wc
    if z >= wc and z >= bc:
        return basic
    else:
        if z < wc and z >= bc:
            return b * bc + w * (bc + z) if w * (bc + z) < w * wc else basic
        elif z < bc and z >= wc:
            return w * wc + b * (wc + z) if b * (wc + z) < b * bc else basic
        else:
            if bc < wc or bc == wc:
                return b * bc + w * (bc + z) if w * (bc + z) < w * wc else basic
            else:
                return w * wc + b * (wc + z) if b * (wc + z) < b * bc else basic

# Better solution
def taumBday(b, w, bc, wc, z):
    return b * min(bc, wc + z) + w * min(wc, bc + z)


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        b, w = map(int, input().strip().split())
        bc, wc, z = map(int, input().strip().split())
        result = taum_bday(b, w, bc, wc, z)
        print(result)
