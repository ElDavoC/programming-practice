from itertools import combinations

def acm_team(topic):
    #par = [str(sum(list(i))).count('0') for i in combinations(topic, 2)]
    print(list(combinations(topic, 2)))
    print([sum([x[0] or x[1] for x in list(zip(*i))]) for i in combinations(topic, 2)])
    #return len(str(topic[0])) - min(par), par.count(min(par))
    return

if __name__ == '__main__':
    #n, m = map(int, input().split())
    #topic = [[int(input().strip())] for _ in range(n)]
    #result = acm_team(topic)
    #print(*result, sep = '\n')

    # Better Solution
    n,k = map(int,input().split())
    teams = [list(map(int,list(input()))) for i in range(n)]
    sums = [sum([x[0] or x[1] for x in list(zip(*i))]) for i in combinations(teams,2)]
    print(max(sums),sums.count(max(sums)),sep = '\n')


    # Explanation
    # print(teams)
    # print(list(combinations(teams, 2)))
    # final = []
    # for i in combinations(teams, 2):
    #     nueva = []
    #     print(list(zip(*i)))
    #     for x in list(zip(*i)):
    #         #print(x[0] or x[1])
    #         nueva.append(x[0] or x[1])
    #
    #     #print(nueva)
    #     final.append(sum(nueva))
    #
    # print(final)
