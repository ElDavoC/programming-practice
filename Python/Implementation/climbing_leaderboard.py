def climbingLeaderboard(ranked, player):
    poss = sorted(list(set(ranked)))
    k = 0
    for i in player:
        for j in range(k, len(poss)):
            if i < poss[j]:
                print(len(poss) - j + 1)
                k = j
                break
            elif i >= poss[j] and j == len(poss) - 1:
                print(1)
    return

if __name__ == '__main__':
    n = int(input())
    ranked = [int(i) for i in input().strip().split()]
    m = int(input())
    player = [int(i) for i in input().strip().split()]

    #result = climbingLeaderboard(ranked, player)

    leaderboard = sorted(set(ranked), reverse = True)
    l = len(leaderboard)

    for a in player:
        while (l > 0) and (a >= leaderboard[l - 1]):
            l -= 1
        print l + 1
