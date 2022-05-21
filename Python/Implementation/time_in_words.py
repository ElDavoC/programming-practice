def time_words(h, m):
    num2words = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 20:'twenty'}
    if m == 0:
        return f"{num2words[h]} o' clock"
    elif m != 30:
        cond = False
        if m > 30:
            cond = True
            m = 60 - m
            h = h + 1 if h < 12 else 1

        try:
            return f"{num2words[m]} {'minutes' if m > 1 else 'minute'} {'past' if not cond else 'to'} {num2words[h]}" if m != 15 else f"quarter {'past' if not cond else 'to'} {num2words[h]}"
        except:
            if m < 20:
                return f"{num2words[int(str(m)[1])]}teen minutes {'past' if not cond else 'to'} {num2words[h]}"
            else:
                return f"twenty {num2words[int(str(m)[1])]} minutes {'past' if not cond else 'to'} {num2words[h]}"
    else:
        return f"half past {num2words[h]}"


if __name__ == '__main__':
    h = int(input().strip())
    m = int(input().strip())
    result = time_words(h, m)
    print(result)
