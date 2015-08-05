def min_coins(n, coins):
    if not n:
        return 0
    if n in coins:
        return 1

    minList = [None for x in range(n+1)]
    minList[0] = []

    for i in xrange(1, n+1):
        if i in coins:
            minList[i] = [i]
            continue
        for c in coins:
            if i > c:
                if not minList[i] or len(minList[i-c]) + 1 < len(minList[i]):
                    minList[i] = minList[i-c] + [c]

        if minList[i] == None:
            return "no solution found"

    return minList[n]


def main():
   print min_coins(29, [1,3,4])

if __name__ == '__main__':
    main()
