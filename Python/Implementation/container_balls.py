def organizing(containers):
    rows = [sum(i) for i in containers]
    cols = [sum(i) for i in zip(*containers)]
    # r_set = set(rows)
    # for i in r_set:
    #     if rows.count(i) != cols.count(i): return 'Impossible'
    #
    # return 'Possible'

    # Better solution
    return 'Possible' if sorted(rows) == sorted(cols) else 'Impossible'


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        containers = [list(map(int, input().strip().split())) for _ in range(int(input().strip()))]
        result = organizing(containers)
        print(result)
