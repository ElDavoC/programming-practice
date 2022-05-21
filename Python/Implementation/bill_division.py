def bon_appetit(bill, k, anna):
    money = anna - (sum(bill[:k] + bill[k + 1:]) // 2)
    return money if money > 0 else 'Bon Appetit'

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    bill = list(map(int, input().strip().split()))
    anna = int(input().strip())
    result = bon_appetit(bill, k, anna)
    print(result)
